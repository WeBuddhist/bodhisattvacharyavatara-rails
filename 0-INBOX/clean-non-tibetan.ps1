<#
clean-non-tibetan.ps1

Removes all non-Tibetan script from a commentary file:
  - page-number lines (e.g. "-486-")
  - garbled OCR running-header lines (legacy-font Wylie)
  - any stray non-Tibetan characters (Latin letters, brackets < > [ ], etc.)

Keeps only Tibetan-block characters (U+0F00-U+0FFF) plus spaces/tabs.
Any line left with no Tibetan after filtering is dropped (page numbers,
OCR headers). Blank lines preserved; 2+ blank lines collapsed to one.

The ORIGINAL file is never modified. Output goes to a ".cleaned.md"
file next to the source so you can review/diff before replacing.

Usage (from the vault root):
    powershell -ExecutionPolicy Bypass -File "0-INBOX\clean-non-tibetan.ps1"
#>

param(
    [string]$Path = "$PSScriptRoot\..\1-SOURCES\Commentaries\bo-རྒྱལ་བ་རིན་པོ་ཆེ།.md"
)

$Path = (Resolve-Path -LiteralPath $Path).Path
if (-not (Test-Path -LiteralPath $Path)) { throw "File not found: $Path" }

$src   = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
$lines = $src -split "`r?`n"

$out         = New-Object System.Collections.Generic.List[string]
$dropped     = 0
$charsBefore = ($src -replace '[\r\n]', '').Length

foreach ($line in $lines) {
    $filtered = $line -replace '[^ༀ-࿿ \t]', ''
    $filtered = ($filtered -replace '[ \t]{2,}', ' ').TrimEnd()

    if ($line.Trim().Length -gt 0 -and ($filtered -notmatch '[ༀ-࿿]')) {
        $dropped++
        continue
    }
    $out.Add($filtered)
}

$text = $out -join "`n"
$text = [regex]::Replace($text, "`n{3,}", "`n`n").Trim() + "`n"

$outPath    = $Path -replace '\.md$', '.cleaned.md'
$utf8NoBom  = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($outPath, $text, $utf8NoBom)

$charsAfter = ($text -replace '[\r\n]', '').Length

Write-Host "Done."
Write-Host "  source : $Path"
Write-Host "  output : $outPath"
Write-Host "  lines dropped (page numbers + OCR headers): $dropped"
Write-Host "  non-Tibetan characters removed            : $($charsBefore - $charsAfter)"
Write-Host ""
Write-Host "Review the .cleaned.md file, then replace the original if it looks right."
