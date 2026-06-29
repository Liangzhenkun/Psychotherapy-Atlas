param(
    [ValidateSet("staged", "repo")]
    [string]$Mode = "staged",

    [int]$WarnFileSizeMB = 5,

    [int]$BlockFileSizeMB = 25
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Section {
    param([string]$Text)
    Write-Host ""
    Write-Host "== $Text ==" -ForegroundColor Cyan
}

function Add-Finding {
    param(
        [System.Collections.Generic.List[object]]$Bucket,
        [string]$Kind,
        [string]$Path,
        [string]$Message
    )

    $Bucket.Add([pscustomobject]@{
        Kind    = $Kind
        Path    = $Path
        Message = $Message
    })
}

function Test-IsBinary {
    param([string]$LiteralPath)

    $stream = [System.IO.File]::OpenRead($LiteralPath)
    try {
        $buffer = New-Object byte[] 4096
        $read = $stream.Read($buffer, 0, $buffer.Length)
        for ($i = 0; $i -lt $read; $i++) {
            if ($buffer[$i] -eq 0) {
                return $true
            }
        }
        return $false
    }
    finally {
        $stream.Dispose()
    }
}

function Get-EffectiveGitEmail {
    $localEmail = (git config --local --get user.email 2>$null)
    if (-not [string]::IsNullOrWhiteSpace($localEmail)) {
        return @{
            Scope = "repository"
            Email = $localEmail.Trim()
        }
    }

    $globalEmail = (git config --global --get user.email 2>$null)
    if (-not [string]::IsNullOrWhiteSpace($globalEmail)) {
        return @{
            Scope = "global"
            Email = $globalEmail.Trim()
        }
    }

    return @{
        Scope = "unset"
        Email = ""
    }
}

function Get-IgnorePatterns {
    param([string]$RepoRoot)

    $ignoreFile = Join-Path $RepoRoot ".repo-guard-ignore"
    if (-not (Test-Path -LiteralPath $ignoreFile)) {
        return @()
    }

    return Get-Content -LiteralPath $ignoreFile -Encoding UTF8 |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ -and -not $_.StartsWith("#") }
}

function Test-IgnoredPath {
    param(
        [string]$RelativePath,
        [string[]]$Patterns
    )

    foreach ($pattern in $Patterns) {
        if ($RelativePath -like $pattern) {
            return $true
        }
    }

    return $false
}

function Get-PathsToScan {
    param([string]$ScanMode)

    if ($ScanMode -eq "staged") {
        $paths = git diff --cached --name-only --diff-filter=ACMR
    }
    else {
        $paths = git ls-files
    }

    return $paths |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ }
}

$repoRoot = (git rev-parse --show-toplevel).Trim()
Set-Location -LiteralPath $repoRoot

$ignorePatterns = Get-IgnorePatterns -RepoRoot $repoRoot
$warnBytes = $WarnFileSizeMB * 1MB
$blockBytes = $BlockFileSizeMB * 1MB

$blockedFindings = New-Object 'System.Collections.Generic.List[object]'
$warningFindings = New-Object 'System.Collections.Generic.List[object]'
$infoFindings = New-Object 'System.Collections.Generic.List[object]'

$blockedNamePatterns = @(
    '(^|/)\.env($|\.)',
    '(^|/)id_rsa$',
    '(^|/)id_ed25519$',
    '\.pem$',
    '\.p12$',
    '\.pfx$',
    '\.jks$',
    '\.key$'
)

$blockedContentPatterns = @(
    @{ Name = "GitHub token"; Regex = 'gh[pousr]_[A-Za-z0-9_]{20,}' },
    @{ Name = "OpenAI-style API key"; Regex = 'sk-[A-Za-z0-9]{20,}' },
    @{ Name = "AWS access key"; Regex = 'AKIA[0-9A-Z]{16}' },
    @{ Name = "Slack token"; Regex = 'xox[baprs]-[A-Za-z0-9-]{10,}' },
    @{ Name = "Private key material"; Regex = '-----BEGIN (RSA |OPENSSH |DSA |EC |PGP )?PRIVATE KEY-----' }
)

$warningContentPatterns = @(
    @{ Name = "Possible secret assignment"; Regex = "(?im)\b(api[_-]?key|secret|token|password)\b.{0,20}[:=].{0,4}['""]?[A-Za-z0-9\/+=_\-]{8,}" },
    @{ Name = "Windows local path"; Regex = '[A-Za-z]:\\Users\\|[A-Za-z]:\\GitProjects\\|\\AppData\\' },
    @{ Name = "POSIX local path"; Regex = '/Users/|/home/[^/\s]+/|/var/folders/|/tmp/' }
)

$textExtensions = @(
    ".txt", ".md", ".html", ".css", ".js", ".json", ".yaml", ".yml", ".xml", ".ps1",
    ".py", ".ts", ".tsx", ".jsx", ".env", ".csv", ".toml", ".ini", ".cfg", ".bib", ".url"
)

$paths = Get-PathsToScan -ScanMode $Mode

foreach ($relativePath in $paths) {
    $normalizedPath = $relativePath.Replace("\", "/")

    if (Test-IgnoredPath -RelativePath $normalizedPath -Patterns $ignorePatterns) {
        continue
    }

    foreach ($pattern in $blockedNamePatterns) {
        if ($normalizedPath -match $pattern) {
            Add-Finding -Bucket $blockedFindings -Kind "file" -Path $normalizedPath -Message "Blocked by filename rule. Use secrets storage or add an explicit ignore entry if this file is intentionally public."
            continue
        }
    }

    $fullPath = Join-Path $repoRoot $relativePath
    if (-not (Test-Path -LiteralPath $fullPath)) {
        continue
    }

    # Dotfiles such as .gitignore are hidden on PowerShell Core runners.
    $item = Get-Item -LiteralPath $fullPath -Force
    if ($item.Length -gt $blockBytes) {
        Add-Finding -Bucket $blockedFindings -Kind "size" -Path $normalizedPath -Message "File is $([math]::Round($item.Length / 1MB, 2)) MB. Move large assets to Git LFS, Releases, or external object storage."
    }
    elseif ($item.Length -gt $warnBytes) {
        Add-Finding -Bucket $warningFindings -Kind "size" -Path $normalizedPath -Message "File is $([math]::Round($item.Length / 1MB, 2)) MB. Large public repo assets are better handled with LFS, Releases, or object storage."
    }

    $extension = [System.IO.Path]::GetExtension($normalizedPath).ToLowerInvariant()
    $shouldScanText = $textExtensions -contains $extension
    if (-not $shouldScanText) {
        continue
    }

    if (Test-IsBinary -LiteralPath $fullPath) {
        continue
    }

    $content = Get-Content -LiteralPath $fullPath -Raw -Encoding UTF8 -Force

    foreach ($rule in $blockedContentPatterns) {
        if ($content -match $rule.Regex) {
            Add-Finding -Bucket $blockedFindings -Kind "content" -Path $normalizedPath -Message "Matched blocked pattern: $($rule.Name)."
        }
    }

    foreach ($rule in $warningContentPatterns) {
        if ($content -match $rule.Regex) {
            Add-Finding -Bucket $warningFindings -Kind "content" -Path $normalizedPath -Message "Matched warning pattern: $($rule.Name)."
        }
    }
}

$gitEmail = Get-EffectiveGitEmail
if ($gitEmail.Scope -eq "unset") {
    Add-Finding -Bucket $warningFindings -Kind "git-config" -Path "(git config)" -Message "No git user.email is configured. Commits may fail attribution checks."
}
elseif ($gitEmail.Email -match '@users\.noreply\.github\.com$') {
    Add-Finding -Bucket $infoFindings -Kind "git-config" -Path "(git config)" -Message "Commit email is using a GitHub noreply address from $($gitEmail.Scope) config."
}
elseif ($gitEmail.Email -match '@(163\.com|qq\.com|gmail\.com|outlook\.com|hotmail\.com|icloud\.com)$') {
    Add-Finding -Bucket $warningFindings -Kind "git-config" -Path "(git config)" -Message "Commit email '$($gitEmail.Email)' looks like a personal address from $($gitEmail.Scope) config. Consider using your GitHub noreply address for public repos."
}
else {
    Add-Finding -Bucket $infoFindings -Kind "git-config" -Path "(git config)" -Message "Commit email is '$($gitEmail.Email)' from $($gitEmail.Scope) config."
}

Write-Section "Repo Guard ($Mode)"
Write-Host "Repository: $repoRoot"

if ($infoFindings.Count -gt 0) {
    Write-Section "Info"
    foreach ($finding in $infoFindings) {
        Write-Host "[INFO] $($finding.Path): $($finding.Message)" -ForegroundColor DarkGray
    }
}

if ($warningFindings.Count -gt 0) {
    Write-Section "Warnings"
    foreach ($finding in $warningFindings) {
        Write-Host "[WARN] $($finding.Path): $($finding.Message)" -ForegroundColor Yellow
    }
}

if ($blockedFindings.Count -gt 0) {
    Write-Section "Blocked"
    foreach ($finding in $blockedFindings) {
        Write-Host "[BLOCK] $($finding.Path): $($finding.Message)" -ForegroundColor Red
    }

    Write-Host ""
    Write-Host "Commit/push blocked by repo guard." -ForegroundColor Red
    Write-Host "If a file is intentionally public, add a narrow path pattern to .repo-guard-ignore after you verify it is safe."
    exit 1
}

Write-Host ""
Write-Host "Repo guard passed." -ForegroundColor Green
