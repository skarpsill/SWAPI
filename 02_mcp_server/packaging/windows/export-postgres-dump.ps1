param(
    [string]$Database = "solidworks_api",
    [string]$User = "postgres",
    [string]$HostName = "localhost",
    [int]$Port = 5432,
    [string]$ApiVersion = "2024",
    [string]$OutputDir = "01_parsing_API\release-assets"
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

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..")
if ([System.IO.Path]::IsPathRooted($OutputDir)) {
    $Out = $OutputDir
}
else {
    $Out = Join-Path $RepoRoot $OutputDir
}
New-Item -ItemType Directory -Force -Path $Out | Out-Null

$DumpPath = Join-Path $Out "solidworks_api_$ApiVersion.dump"
$PgDump = Find-PostgresTool "pg_dump"

& $PgDump `
    --host $HostName `
    --port $Port `
    --username $User `
    --format custom `
    --compress 9 `
    --no-owner `
    --no-privileges `
    --file $DumpPath `
    $Database

Write-Host "PostgreSQL dump:"
Write-Host $DumpPath
