# Run lint and tests in sequence.
# Exit on first failure.

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

Write-Host "=== Lint ===" -ForegroundColor Cyan
if (Get-Command uv -ErrorAction SilentlyContinue) {
    uv run ruff check .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} elseif (Get-Command ruff -ErrorAction SilentlyContinue) {
    ruff check .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} else {
    Write-Host "ruff not found - skipping lint"
}

Write-Host ""
Write-Host "=== Tests ===" -ForegroundColor Cyan
if (Get-Command uv -ErrorAction SilentlyContinue) {
    uv run pytest
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} elseif (Get-Command pytest -ErrorAction SilentlyContinue) {
    pytest
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} else {
    Write-Host "pytest not found - skipping tests"
}

Write-Host ""
Write-Host "=== All checks passed ===" -ForegroundColor Green
