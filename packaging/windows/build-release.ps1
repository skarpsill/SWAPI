param(
    [string]$Version = "0.1.0",
    [string]$ApiVersion = "2024",
    [string]$DatabaseDump = "",
    [string]$OutputDir = "dist"
)

$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$Python = Join-Path $Root ".venv\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    throw "Virtual environment not found. Create it first: python -m venv .venv"
}

& $Python -m pip install -e ".[postgres,release]"

$BuildRoot = Join-Path $Root $OutputDir
$PackageName = "solidworks-api-mcp-$Version-windows-x64"
$PackageDir = Join-Path $BuildRoot $PackageName
$ExeWork = Join-Path $BuildRoot "pyinstaller-work"

New-Item -ItemType Directory -Force -Path $BuildRoot | Out-Null
if (Test-Path $PackageDir) {
    Remove-Item -Recurse -Force -LiteralPath $PackageDir
}
New-Item -ItemType Directory -Force -Path $PackageDir | Out-Null

& $Python -m PyInstaller `
    --clean `
    --noconfirm `
    --onefile `
    --name swapi-mcp-server `
    --distpath $PackageDir `
    --workpath $ExeWork `
    (Join-Path $Root "packaging\pyinstaller\swapi_mcp_server.py")

Copy-Item -LiteralPath (Join-Path $Root "packaging\windows\install.ps1") -Destination $PackageDir
Copy-Item -LiteralPath (Join-Path $Root "packaging\windows\restore-db.ps1") -Destination $PackageDir
Copy-Item -LiteralPath (Join-Path $Root "packaging\windows\README.md") -Destination $PackageDir

if ($DatabaseDump) {
    if (-not (Test-Path $DatabaseDump)) {
        throw "Database dump not found: $DatabaseDump"
    }
    Copy-Item -LiteralPath $DatabaseDump -Destination (Join-Path $PackageDir "solidworks_api_$ApiVersion.dump")
}

$ZipPath = Join-Path $BuildRoot "$PackageName.zip"
if (Test-Path $ZipPath) {
    Remove-Item -Force -LiteralPath $ZipPath
}
Compress-Archive -Path (Join-Path $PackageDir "*") -DestinationPath $ZipPath

Write-Host "Release package:"
Write-Host $ZipPath
