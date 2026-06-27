param(
    [string]$InstallDir = "$env:LOCALAPPDATA\Programs\SolidWorksApiMcp",
    [string]$Database = "solidworks_api",
    [string]$DatabaseUser = "postgres",
    [string]$DatabaseHost = "localhost",
    [int]$DatabasePort = 5432,
    [switch]$SkipDatabaseRestore
)

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null

Copy-Item -LiteralPath (Join-Path $PSScriptRoot "swapi-mcp-server.exe") -Destination $InstallDir -Force
Copy-Item -LiteralPath (Join-Path $PSScriptRoot "restore-db.ps1") -Destination $InstallDir -Force
Copy-Item -LiteralPath (Join-Path $PSScriptRoot "README.md") -Destination $InstallDir -Force

if (-not $SkipDatabaseRestore) {
    & (Join-Path $PSScriptRoot "restore-db.ps1") `
        -Database $Database `
        -User $DatabaseUser `
        -HostName $DatabaseHost `
        -Port $DatabasePort
}

$ExePath = Join-Path $InstallDir "swapi-mcp-server.exe"
$DatabaseUrl = "postgresql://$DatabaseUser@$DatabaseHost`:$DatabasePort/$Database"

Write-Host ""
Write-Host "Installed SOLIDWORKS API MCP server:"
Write-Host $ExePath
Write-Host ""
Write-Host "MCP server config snippet:"
Write-Host "{"
Write-Host '  "mcpServers": {'
Write-Host '    "solidworks-api": {'
Write-Host "      `"command`": `"$ExePath`","
Write-Host '      "env": {'
Write-Host "        `"SWAPI_DATABASE_URL`": `"$DatabaseUrl`","
Write-Host '        "SWAPI_DEFAULT_VERSION": "2024"'
Write-Host '      }'
Write-Host '    }'
Write-Host '  }'
Write-Host "}"
