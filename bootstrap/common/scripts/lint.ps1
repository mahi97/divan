$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

if (Get-Command ruff -ErrorAction SilentlyContinue) {
    ruff check @args .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} else {
    Write-Host "ruff not found. Install with: pip install ruff" -ForegroundColor Red
    exit 1
}
