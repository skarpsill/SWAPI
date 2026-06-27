param(
    [string]$InstallDir = "$env:LOCALAPPDATA\Programs\SolidWorksApiMcp",
    [string]$Database = "solidworks_api",
    [string]$DatabaseUser = "postgres",
    [string]$DatabaseHost = "localhost",
    [int]$DatabasePort = 5432,
    [string]$ApiVersion = "2024",
    [switch]$SkipDatabaseRestore,
    [switch]$ConfigureCodex,
    [string]$CodexConfigPath = "$env:USERPROFILE\.codex\config.toml",
    [switch]$ConfigureVsCode,
    [string]$VsCodeMcpConfigPath = "$env:APPDATA\Code\User\mcp.json"
)

$ErrorActionPreference = "Stop"

function ConvertTo-TomlLiteral([string]$Value) {
    if ($Value -notmatch "'") {
        return "'" + $Value + "'"
    }

    $Escaped = $Value -replace "\\", "\\" -replace '"', '\"'
    return '"' + $Escaped + '"'
}

function Set-CodexMcpServerConfig(
    [string]$ConfigPath,
    [string]$ServerName,
    [string]$Command,
    [hashtable]$Env
) {
    $ConfigDir = Split-Path -Parent $ConfigPath
    if ($ConfigDir) {
        New-Item -ItemType Directory -Force -Path $ConfigDir | Out-Null
    }

    $EnvParts = @()
    foreach ($Key in ($Env.Keys | Sort-Object)) {
        $EnvParts += "$Key = $(ConvertTo-TomlLiteral $Env[$Key])"
    }

    $Block = @(
        "[mcp_servers.$ServerName]",
        "command = $(ConvertTo-TomlLiteral $Command)",
        "env = { $($EnvParts -join ', ') }"
    ) -join [Environment]::NewLine

    $Existing = ""
    if (Test-Path -LiteralPath $ConfigPath) {
        $Existing = Get-Content -LiteralPath $ConfigPath -Raw
    }

    $Pattern = "(?ms)^\[mcp_servers\.$([regex]::Escape($ServerName))\]\r?\n.*?(?=^\[|\z)"
    if ($Existing -match $Pattern) {
        $Updated = [regex]::Replace($Existing, $Pattern, $Block)
    }
    elseif ($Existing.Trim()) {
        $Updated = $Existing.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $Block + [Environment]::NewLine
    }
    else {
        $Updated = $Block + [Environment]::NewLine
    }

    Set-Content -LiteralPath $ConfigPath -Value $Updated -Encoding UTF8
}

function Set-VsCodeMcpServerConfig(
    [string]$ConfigPath,
    [string]$ServerName,
    [string]$Command,
    [hashtable]$Env
) {
    $ConfigDir = Split-Path -Parent $ConfigPath
    if ($ConfigDir) {
        New-Item -ItemType Directory -Force -Path $ConfigDir | Out-Null
    }

    if (Test-Path -LiteralPath $ConfigPath) {
        $Raw = Get-Content -LiteralPath $ConfigPath -Raw
        if ($Raw.Trim()) {
            $Config = $Raw | ConvertFrom-Json
        }
        else {
            $Config = [pscustomobject]@{}
        }
    }
    else {
        $Config = [pscustomobject]@{}
    }

    if (-not ($Config.PSObject.Properties.Name -contains "mcpServers")) {
        $Config | Add-Member -MemberType NoteProperty -Name "mcpServers" -Value ([pscustomobject]@{})
    }

    $EnvObject = [ordered]@{}
    foreach ($Key in ($Env.Keys | Sort-Object)) {
        $EnvObject[$Key] = $Env[$Key]
    }

    $ServerConfig = [pscustomobject]@{
        command = $Command
        env = [pscustomobject]$EnvObject
    }

    if ($Config.mcpServers.PSObject.Properties.Name -contains $ServerName) {
        $Config.mcpServers.$ServerName = $ServerConfig
    }
    else {
        $Config.mcpServers | Add-Member -MemberType NoteProperty -Name $ServerName -Value $ServerConfig
    }

    $Config | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $ConfigPath -Encoding UTF8
}

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
$McpEnv = @{
    SWAPI_DATABASE_URL = $DatabaseUrl
    SWAPI_DEFAULT_VERSION = $ApiVersion
}

if ($ConfigureCodex) {
    Set-CodexMcpServerConfig `
        -ConfigPath $CodexConfigPath `
        -ServerName "solidworks-api" `
        -Command $ExePath `
        -Env $McpEnv
}

if ($ConfigureVsCode) {
    Set-VsCodeMcpServerConfig `
        -ConfigPath $VsCodeMcpConfigPath `
        -ServerName "solidworks-api" `
        -Command $ExePath `
        -Env $McpEnv
}

Write-Host ""
Write-Host "Installed SOLIDWORKS API MCP server:"
Write-Host $ExePath
Write-Host ""
if ($ConfigureCodex) {
    Write-Host "Updated Codex MCP config:"
    Write-Host $CodexConfigPath
    Write-Host ""
}
if ($ConfigureVsCode) {
    Write-Host "Updated VS Code MCP config:"
    Write-Host $VsCodeMcpConfigPath
    Write-Host ""
}
Write-Host "MCP server config snippet:"
Write-Host "[mcp_servers.solidworks-api]"
Write-Host "command = $(ConvertTo-TomlLiteral $ExePath)"
Write-Host "env = { SWAPI_DATABASE_URL = $(ConvertTo-TomlLiteral $DatabaseUrl), SWAPI_DEFAULT_VERSION = $(ConvertTo-TomlLiteral $ApiVersion) }"
