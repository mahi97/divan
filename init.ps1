# init.ps1 — Initialize the parent project from divan bootstrap files.
#
# Run from anywhere inside a project that contains divan/:
#   cd my_project\divan; .\init.ps1
#   cd my_project; .\divan\init.ps1
#
# Options are passed through to tools/init_project.py.
#
# Examples:
#   .\init.ps1
#   .\init.ps1 --profile llm-research
#   .\init.ps1 --dry-run
#   .\init.ps1 --force --backup

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Ensure we're running from divan root
if (-not (Test-Path "$ScriptDir\tools\init_project.py")) {
    Write-Error "Cannot find tools/init_project.py. Are you running from divan/?"
    exit 1
}

# Require python
$pythonCmd = if (Get-Command python -ErrorAction SilentlyContinue) { "python" }
             elseif (Get-Command python3 -ErrorAction SilentlyContinue) { "python3" }
             else { $null }

if (-not $pythonCmd) {
    Write-Error "python not found. Please install Python 3.8+."
    exit 1
}

$TargetDir = Split-Path -Parent $ScriptDir

Write-Host "=== Divan Init ===" -ForegroundColor Cyan
Write-Host "Divan root:     $ScriptDir"
Write-Host "Target project: $TargetDir"
Write-Host ""

& $pythonCmd "$ScriptDir\tools\init_project.py" @args
$status = $LASTEXITCODE

if ($status -eq 0) {
    Write-Host ""
    Write-Host "=== Done ===" -ForegroundColor Green
    Write-Host "Next steps:"
    Write-Host "  1. Fill in your server details in divan\docs\servers\"
    Write-Host "  2. Create a Python venv: python -m venv .venv"
    Write-Host "  3. Run: scripts\check.ps1"
}

exit $status
