param(
    [string]$Tag,
    [string]$Title = "",
    [string]$PackagePath,
    [switch]$Draft
)

$ErrorActionPreference = "Stop"

if (-not $Tag) {
    throw "Pass -Tag, for example: -Tag v0.1.0"
}
if (-not $PackagePath -or -not (Test-Path $PackagePath)) {
    throw "Pass -PackagePath pointing to the release zip."
}

$Gh = Get-Command gh -ErrorAction SilentlyContinue
if (-not $Gh) {
    throw "GitHub CLI 'gh' was not found. Install it or create the release in GitHub UI."
}

if (-not $Title) {
    $Title = "SOLIDWORKS API MCP Server $Tag"
}

$Args = @("release", "create", $Tag, $PackagePath, "--title", $Title, "--notes-file", "docs/PRODUCT_RELEASE.md")
if ($Draft) {
    $Args += "--draft"
}

& $Gh.Source @Args
