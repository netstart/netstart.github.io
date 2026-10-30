# Aponta os hooks deste repositório para a pasta versionada .githooks.
Set-Location (Join-Path $PSScriptRoot "..")
git config core.hooksPath .githooks
if ($LASTEXITCODE -eq 0) { Write-Host "Hooks instalados: core.hooksPath = .githooks" }
