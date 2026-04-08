$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

if (Get-Command pytest -ErrorAction SilentlyContinue) {
    pytest @args
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} else {
    Write-Host "pytest not found. Install with: pip install pytest" -ForegroundColor Red
    exit 1
}
