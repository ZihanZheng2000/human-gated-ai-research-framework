import csv
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / "research" / "ai-role-paper-comprehension-water-resources"
VALIDATION = PROJECT / "artifacts" / "validation"
TABLES = PROJECT / "artifacts" / "tables"
DATA = PROJECT / "artifacts" / "data" / "cleaned"
LOGS = PROJECT / "artifacts" / "logs"

MODEL = os.environ.get("OPENAI_AGENT_GROUP_MODEL", "gpt-4o-mini")
SEED = int(os.environ.get("AGENT_GROUP_SEED", "20260705"))
MAX_OUTPUT_TOKENS = int(os.environ.get("AGENT_GROUP_MAX_OUTPUT_TOKENS", "1200"))


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def compact_article_packet() -> str:
    text = (DATA / "hess-20-3631-2016_clean_text.txt").read_text(encoding="utf-8")
    headings = []
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = {"heading": line[3:].strip(), "body": []}
            headings.append(current)
        elif current is not None and line.strip():
            current["body"].append(line.strip())

    selected = []
    keep = {
        "Abstract",
        "Introduction",
        "Drought as a lack of water",
        "Drier than normal: timescales of drought in the Anthropocene",
        "Confusion between terms in the Anthropocene",
        "A framework for understanding and analysing drought in the Anthropocene",
        "Drivers of drought",
        "Modifications of drought",
        "Impacts of drought",
        "Human feedback of drought",
        "Changing the normal situation",
        "A broader scope on drought in the Anthropocene",
    }
    for item in headings:
        if item["heading"] not in keep:
            continue
        body = " ".join(item["body"])
        selected.append(f"## {item['heading']}\n{body[:900]}")
    return "\n\n".join(selected)


def read_questions() -> list[dict]:
    with (VALIDATION / "question_ladder.csv").open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def read_hints() -> dict[str, str]:
    text = (VALIDATION / "author_hints.md").read_text(encoding="utf-8")
    hints = {}
    for line in text.splitlines():
        if not line.startswith("| Q"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) >= 2:
            hints[parts[0]] = parts[1]
    return hints


ROLES = {
    "R1": {
        "name": "Undergraduate",
        "knowledge": "introductory environmental science and water-resources coursework; limited research-paper reading experience",
        "error_rate": 0.35,
        "style": "plain, sometimes incomplete, may confuse close terms",
    },
    "R2": {
        "name": "Master",
        "knowledge": "graduate coursework in hydrology or water resources; some paper-reading experience",
        "error_rate": 0.22,
        "style": "moderately technical, usually gets main ideas but may miss deeper assumptions",
    },
    "R3": {
        "name": "PhD",
        "knowledge": "doctoral-level hydrology or socio-hydrology training; strong method and literature awareness",
        "error_rate": 0.10,
        "style": "technical and careful, may still miss some operational details",
    },
    "R4": {
        "name": "Advisor",
        "knowledge": "senior water-resources researcher; expert in conceptual frameworks, attribution, and research design",
        "error_rate": 0.04,
        "style": "expert critique, distinguishes direct evidence from gaps",
    },
}


def response_text(payload: dict) -> str:
    chunks = []
    for item in payload.get("output", []):
        for content in item.get("content", []):
            if content.get("type") in {"output_text", "text"} and "text" in content:
                chunks.append(content["text"])
    if chunks:
        return "\n".join(chunks)
    if "output_text" in payload:
        return payload["output_text"]
    return json.dumps(payload)


def call_openai(system: str, user: str) -> tuple[str, dict]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured")

    body = {
        "model": MODEL,
        "input": [
            {"role": "system", "content": [{"type": "input_text", "text": system}]},
            {"role": "user", "content": [{"type": "input_text", "text": user}]},
        ],
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "text": {"format": {"type": "json_object"}},
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API HTTP {exc.code}: {detail}") from exc
    return response_text(payload), payload.get("usage", {})


def extract_json(text: str):
    match = re.search(r"\{.*\}", text, flags=re.S)
    if not match:
        raise ValueError(f"No JSON object found in model output: {text[:300]}")
    return json.loads(match.group(0))


def reader_system(role_id: str, role: dict, round_name: str, mistake_ids: list[str]) -> str:
    return f"""You are simulated reader {role_id}: {role['name']}.
Knowledge boundary: {role['knowledge']}.
Behavior style: {role['style']}.
This is an isolated API call. You do not share memory with other readers or with the evaluator.
You may use only the article packet provided in this call and your stated knowledge profile.
You are not completely ignorant, but your role has bounded knowledge. If a question is marked likely_mistake, answer naturally with the kind of partial misunderstanding this role might have; do not intentionally be absurd.
Round: {round_name}. Questions marked likely_mistake for this role and round: {', '.join(mistake_ids) if mistake_ids else 'none'}.
Return strict JSON only:
{{"role_id":"{role_id}","round":"{round_name}","answers":[{{"question_id":"Q1","answer":"..."}}]}}
"""


def evaluator_system() -> str:
    return """You are an isolated author/evaluator grounded in the article packet and answer key.
Score article comprehension, not prose confidence. Do not reward unsupported external speculation.
Use integer scores from 0 to 4:
0 no relevant understanding; 1 one relevant idea but main logic missing; 2 partially correct; 3 mostly correct; 4 complete and well grounded.
Return strict JSON only:
{"scores":[{"question_id":"Q1","score":0,"reason":"..."}]}
"""


def main() -> int:
    load_env_file(ROOT / ".env.local")
    random.seed(SEED)
    TABLES.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)

    article = compact_article_packet()
    questions = read_questions()
    hints = read_hints()
    question_text = "\n".join(
        f"{q['question_id']} ({q['difficulty_tier']}): {q['question']}" for q in questions
    )
    answer_key = "\n".join(
        f"{q['question_id']}: {q['expected_components']}" for q in questions
    )

    run_records = []
    score_rows = []
    usage_rows = []

    for role_id, role in ROLES.items():
        for round_name in ["pre", "post"]:
            mistake_ids = [
                q["question_id"]
                for q in questions
                if random.random() < role["error_rate"] * (0.55 if round_name == "post" else 1.0)
            ]
            hints_block = ""
            if round_name == "post":
                hints_block = "\nHints:\n" + "\n".join(f"{qid}: {hint}" for qid, hint in hints.items())
            system = reader_system(role_id, role, round_name, mistake_ids)
            user = f"""Article packet:
{article}

Questions:
{question_text}
{hints_block}
"""
            text, usage = call_openai(system, user)
            usage_rows.append({"agent": role_id, "round": round_name, "usage": usage})
            answers_obj = extract_json(text)
            answers = answers_obj["answers"]
            run_records.append(
                {
                    "role_id": role_id,
                    "role_name": role["name"],
                    "round": round_name,
                    "mistake_ids": mistake_ids,
                    "answers": answers,
                }
            )

            eval_user = f"""Article packet:
{article}

Answer key:
{answer_key}

Reader role: {role_id} {role['name']}
Round: {round_name}
Reader answers:
{json.dumps(answers, ensure_ascii=False)}
"""
            score_text, score_usage = call_openai(evaluator_system(), eval_user)
            usage_rows.append({"agent": "A1_evaluator", "round": f"{role_id}_{round_name}", "usage": score_usage})
            scores_obj = extract_json(score_text)
            score_map = {s["question_id"]: s for s in scores_obj["scores"]}
            answer_map = {a["question_id"]: a["answer"] for a in answers}
            for q in questions:
                qid = q["question_id"]
                s = score_map[qid]
                score_rows.append(
                    {
                        "role_id": role_id,
                        "role_name": role["name"],
                        "question_id": qid,
                        "round": round_name,
                        "likely_mistake": "yes" if qid in mistake_ids else "no",
                        "score": int(s["score"]),
                        "score_reason": s["reason"],
                        "answer": answer_map.get(qid, ""),
                    }
                )
            time.sleep(0.2)

    out_json = TABLES / "openai_agent_group_raw_outputs.json"
    out_csv = TABLES / "openai_agent_group_scores.csv"
    out_summary = TABLES / "openai_agent_group_summary.csv"
    out_usage = LOGS / "openai_agent_group_usage.json"

    out_json.write_text(json.dumps(run_records, ensure_ascii=False, indent=2), encoding="utf-8")
    out_usage.write_text(json.dumps(usage_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "role_id",
                "role_name",
                "question_id",
                "round",
                "likely_mistake",
                "score",
                "score_reason",
                "answer",
            ],
        )
        writer.writeheader()
        writer.writerows(score_rows)

    summary_rows = []
    for role_id, role in ROLES.items():
        rows = [r for r in score_rows if r["role_id"] == role_id]
        pre = sum(r["score"] for r in rows if r["round"] == "pre")
        post = sum(r["score"] for r in rows if r["round"] == "post")
        summary_rows.append(
            {
                "role_id": role_id,
                "role_name": role["name"],
                "model": MODEL,
                "pre_total": pre,
                "post_total": post,
                "delta_total": post - pre,
                "pre_avg": round(pre / 10, 2),
                "post_avg": round(post / 10, 2),
                "delta_avg": round((post - pre) / 10, 2),
            }
        )
    with out_summary.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    print(json.dumps({"model": MODEL, "summary": summary_rows}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
