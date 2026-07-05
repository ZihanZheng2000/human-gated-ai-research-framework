import json
import os
import urllib.error
import urllib.request
from pathlib import Path


root = Path(__file__).resolve().parents[4]
for line in (root / ".env.local").read_text(encoding="utf-8").splitlines():
    if line.strip().startswith("OPENAI_API_KEY="):
        os.environ["OPENAI_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")

body = {
    "model": "gpt-4o-mini",
    "input": "Return JSON: {\"ok\": true}",
    "max_output_tokens": 32,
    "text": {"format": {"type": "json_object"}},
}
req = urllib.request.Request(
    "https://api.openai.com/v1/responses",
    data=json.dumps(body).encode("utf-8"),
    headers={
        "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        print("status", resp.status)
        print(resp.read().decode("utf-8")[:500])
except urllib.error.HTTPError as exc:
    print("status", exc.code)
    print(exc.read().decode("utf-8", errors="replace")[:1000])
