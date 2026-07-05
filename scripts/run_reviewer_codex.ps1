param(
    [Parameter(Mandatory = $true)]
    [string]$ReviewRequestPath,

    [string]$CritiquePath,

    [string]$CodexCommand = "codex",

    [switch]$Overwrite
)

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$requestFullPath = (Resolve-Path -LiteralPath $ReviewRequestPath).Path

if (-not $CritiquePath) {
    $requestDir = Split-Path -Parent $requestFullPath
    $CritiquePath = Join-Path $requestDir "reviewer-critique.md"
}

$critiqueFullPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($CritiquePath)
if ((Test-Path -LiteralPath $critiqueFullPath) -and -not $Overwrite) {
    throw "Critique file already exists: $critiqueFullPath. Pass -Overwrite to replace it."
}

$prompt = @"
You are the reviewer agent for this repository.

Work from this repository root:
$repoRoot

Required behavior:
1. Read WORKFLOW-CONFIG.md to confirm the active configuration and whether Codex is currently the reviewer.
2. Read AGENTS.md.
3. Read docs/reviewer-agents/cross-agent-handoff.md.
4. Read this review request:
$requestFullPath
5. If WORKFLOW-CONFIG does not assign Codex as reviewer, still write a critique file to the exact path below, but make the first finding a blocker that says the active configuration does not authorize Codex as reviewer.
6. If Codex is the reviewer, read the stage package and supporting artifacts listed in the review request.
7. If Codex is the reviewer, read the relevant stage reviewer-agent file named by the review request stage.
8. Write your critique to this exact path:
$critiqueFullPath

Use the critique table format required by the reviewer-agent instructions.
Do not edit the stage package, docs, templates, or supporting artifacts.
If the request is incomplete, still write reviewer-critique.md and record the blocker.
"@

Push-Location $repoRoot
try {
    & $CodexCommand exec -C $repoRoot --sandbox workspace-write $prompt
    $exitCode = $LASTEXITCODE
}
finally {
    Pop-Location
}

if ($exitCode -ne 0) {
    throw "Codex reviewer command failed with exit code $exitCode."
}

if (-not (Test-Path -LiteralPath $critiqueFullPath)) {
    throw "Codex command completed, but critique file was not created: $critiqueFullPath"
}

Write-Output "Reviewer critique written: $critiqueFullPath"
