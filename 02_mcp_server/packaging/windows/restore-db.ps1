param(
    [string]$Database = "solidworks_api",
    [string]$User = "postgres",
    [string]$HostName = "localhost",
    [int]$Port = 5432,
    [string]$DumpPath = "",
    [switch]$DropExisting
)

$ErrorActionPreference = "Stop"

function Find-PostgresTool([string]$Name) {
    $Command = Get-Command $Name -ErrorAction SilentlyContinue
    if ($Command) {
        return $Command.Source
    }

    $Candidates = @(
        "C:\Program Files\PostgreSQL\18\bin\$Name.exe",
        "C:\Program Files\PostgreSQL\17\bin\$Name.exe",
        "C:\Program Files\PostgreSQL\16\bin\$Name.exe",
        "C:\Program Files\PostgreSQL\15\bin\$Name.exe"
    )
    foreach ($Candidate in $Candidates) {
        if (Test-Path $Candidate) {
            return $Candidate
        }
    }
    throw "$Name was not found. Install PostgreSQL or add its bin directory to PATH."
}

if (-not $DumpPath) {
    $DumpPath = Get-ChildItem -Path $PSScriptRoot -Filter "solidworks_api_*.dump" |
        Select-Object -First 1 -ExpandProperty FullName
}
if (-not $DumpPath -or -not (Test-Path $DumpPath)) {
    throw "Database dump not found. Put solidworks_api_<version>.dump next to this script or pass -DumpPath."
}

$Psql = Find-PostgresTool "psql"
$PgRestore = Find-PostgresTool "pg_restore"

if ($DropExisting) {
    & $Psql --host $HostName --port $Port --username $User --dbname postgres --command "DROP DATABASE IF EXISTS $Database"
}

& $Psql --host $HostName --port $Port --username $User --dbname postgres --command "SELECT 1 FROM pg_database WHERE datname = '$Database'" |
    Out-Null

$Exists = & $Psql --host $HostName --port $Port --username $User --dbname postgres --tuples-only --no-align --command "SELECT 1 FROM pg_database WHERE datname = '$Database'"
if (-not $Exists) {
    & $Psql --host $HostName --port $Port --username $User --dbname postgres --command "CREATE DATABASE $Database"
}

& $PgRestore `
    --host $HostName `
    --port $Port `
    --username $User `
    --dbname $Database `
    --clean `
    --if-exists `
    --no-owner `
    --no-privileges `
    $DumpPath

Write-Host "Database restored: $Database"
