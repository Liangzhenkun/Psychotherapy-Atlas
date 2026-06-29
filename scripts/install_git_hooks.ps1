Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (git rev-parse --show-toplevel).Trim()
Set-Location -LiteralPath $repoRoot

git config core.hooksPath .githooks

Write-Host "Installed repository hooks path: .githooks" -ForegroundColor Green
Write-Host "Pre-commit and pre-push checks will now run automatically in this repository."
