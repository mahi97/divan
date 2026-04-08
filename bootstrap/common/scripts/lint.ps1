$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

if (Get-Command uv -ErrorAction SilentlyContinue) {
    uv run ruff check @args .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} elseif (Get-Command ruff -ErrorAction SilentlyContinue) {
    ruff check @args .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} else {
    Write-Host "ruff not found. Install with: uv sync --extra dev" -ForegroundColor Red
    exit 1
}
