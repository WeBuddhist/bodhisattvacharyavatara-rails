@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

:: ================================================================
:: Dharma Verse Practice Generator — Gemini API Caller
:: ================================================================
:: Usage:   call-gemini.bat verses.txt [output.txt]
:: Example: call-gemini.bat my_verses.txt result.txt
::
:: Before running, set your API key:
::   set GEMINI_API_KEY=AIza...yourkey...
:: Or add it permanently via System Properties > Environment Variables
::
:: Requires: curl (built into Windows 10+), PowerShell 5+
:: ================================================================

set "MODEL=gemini-2.0-flash"
set "API_URL=https://generativelanguage.googleapis.com/v1beta/models/%MODEL%:generateContent"

:: ── Check API key ────────────────────────────────────────────────
if "%GEMINI_API_KEY%"=="" (
    echo.
    echo  [ERROR] GEMINI_API_KEY is not set.
    echo.
    echo  Set it now by running:
    echo    set GEMINI_API_KEY=AIza...your_key_here...
    echo.
    echo  Or add it permanently in:
    echo    Control Panel ^> System ^> Advanced ^> Environment Variables
    echo.
    exit /b 1
)

:: ── Check input file ─────────────────────────────────────────────
if "%~1"=="" (
    echo.
    echo  Usage:   %~nx0 verses.txt [output.txt]
    echo  Example: %~nx0 spyod_jug.txt result.txt
    echo.
    echo  The input file should contain the Tibetan verses, one per block.
    echo.
    exit /b 1
)

if not exist "%~1" (
    echo.
    echo  [ERROR] Input file not found: %~1
    echo.
    exit /b 1
)

set "INPUT_FILE=%~1"
set "OUTPUT_FILE=%~2"
if "%OUTPUT_FILE%"=="" set "OUTPUT_FILE=dharma_practices.txt"

set "TEMP_PS1=%TEMP%\gemini_call.ps1"
set "TEMP_RESPONSE=%TEMP%\gemini_response.json"

echo.
echo  ================================================================
echo   Dharma Verse Practice Generator
echo   Model : %MODEL%
echo   Input : %INPUT_FILE%
echo   Output: %OUTPUT_FILE%
echo  ================================================================
echo.

:: ── Write PowerShell script to temp file ─────────────────────────
:: (Avoids BAT quoting nightmares with complex strings)
(
echo $ErrorActionPreference = 'Stop'
echo $apiKey  = $env:GEMINI_API_KEY
echo $apiUrl  = '%API_URL%'
echo $inFile  = '%INPUT_FILE%'
echo $outFile = '%OUTPUT_FILE%'
echo $respFile = '%TEMP_RESPONSE%'
echo.
echo # Read verses from file
echo $verses = [System.IO.File]::ReadAllText($inFile, [System.Text.Encoding]::UTF8^)
echo.
echo # Build system prompt
echo $systemPrompt = @"
echo You are a Buddhist dharma teacher specializing in Shantideva's Bodhicaryavatara (spyod 'jug).
echo.
echo For each verse provided, generate a trilingual daily practice and explanation following these STRICT rules:
echo.
echo OUTPUT FORMAT (for each verse):
echo 1. Show all four verse lines first
echo 2. Then write in this exact order: Tibetan, then English, then Hindi
echo.
echo RULES FOR PRACTICE (lag len):
echo - Must be ONE concrete action doable TODAY in ordinary life (not a vague aspiration)
echo - Under 20 Tibetan syllables (equivalent brevity in English/Hindi)
echo - Must relate to one of: avoiding evil / doing good / taming mind / generosity / ethics / patience / diligence / meditation / wisdom
echo - Label: Tibetan: lag len (ལག་ལེན།)   English: Practice:   Hindi: abhyas (अभ्यास:)
echo.
echo RULES FOR EXPLANATION (grel bshad):
echo - Under 40 Tibetan syllables (equivalent brevity in English/Hindi)
echo - Explain how TODAY's specific practice enacts THIS verse's teaching
echo - Reference what the verse actually says — not a generic spiritual statement
echo - Label: Tibetan: grel bshad (འགྲེལ་བཤད།)   English: Explanation:   Hindi: vyakhya (व्याख्या:)
echo.
echo EXAMPLE OUTPUT (for one verse):
echo.
echo ### tsigs bcad 1 (ཚིགས་བཅད་ ༡ །)
echo sems can rnams kyi klad nad tsam / /
echo bsal lo snyam du bsams na yang / /
echo phan 'dogs bsam pa dang ldan de / /
echo bsod nams dpag med ldan gyur na / /
echo.
echo **Tibetan:**
echo ལག་ལེན། དེ་རིང་སྐར་མ་ལྔ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་བསལ་འདོད་ཀྱི་ཐུགས་རྗེའི་བསམ་བློ་གཏོང་རྒྱུ་ཡིན།
echo འགྲེལ་བཤད། སེམས་ཅན་ཀུན་གྱི་ཀླད་ནད་ཙམ་བསལ་ལོ་སྙམ་བསམས་ན་བསོད་ནམས་དཔག་མེད་ལྡན་ཞེས་གསུངས། གཞན་གྱི་སྡུག་བསྔལ་སེལ་འདོད་ཀྱི་ཐུགས་རྗེ་ཉམས་སུ་ལེན་པ་ཁོ་ན་ཡིས་བསམ་གཏན་ཚད་ལྡན་ཡིན།
echo.
echo **English:**
echo Practice: Today I will spend five minutes sincerely wishing for all beings to be free from suffering.
echo Explanation: This verse says that even simply thinking "I will relieve beings' headaches" brings immeasurable merit. Five minutes of sincere loving-kindness is complete meditation embodied.
echo.
echo **Hindi:**
echo अभ्यास: आज मैं पाँच मिनट सभी प्राणियों को दुःख से मुक्त देखने की सच्ची कामना में बिताऊँगा।
echo व्याख्या: यह श्लोक कहता है कि केवल "मैं प्राणियों के सिरदर्द दूर करूँगा" सोचने मात्र से असीम पुण्य मिलता है। पाँच मिनट की सच्ची करुणा-भावना पूर्ण ध्यान का साकार रूप है।
echo "@
echo.
echo # Build request body
echo $body = @{
echo     system_instruction = @{
echo         parts = @(@{ text = $systemPrompt }^)
echo     }
echo     contents = @(
echo         @{
echo             role = 'user'
echo             parts = @(@{ text = "Please generate practices and explanations for these verses:`n`n$verses" }^)
echo         }
echo     ^)
echo     generationConfig = @{
echo         temperature     = 0.3
echo         maxOutputTokens = 8192
echo     }
echo } ^| ConvertTo-Json -Depth 10
echo.
echo # Call Gemini API
echo Write-Host "  Calling Gemini API..." -ForegroundColor Cyan
echo $response = Invoke-WebRequest `
echo     -Uri "${apiUrl}?key=${apiKey}" `
echo     -Method Post `
echo     -ContentType 'application/json; charset=utf-8' `
echo     -Body ([System.Text.Encoding]::UTF8.GetBytes($body^)^) `
echo     -UseBasicParsing
echo.
echo # Parse response
echo $json = $response.Content ^| ConvertFrom-Json
echo if ($json.error^) {
echo     Write-Host "`n  [API ERROR] $($json.error.message^)" -ForegroundColor Red
echo     exit 1
echo }
echo.
echo $text = $json.candidates[0].content.parts[0].text
echo.
echo # Save output
echo [System.IO.File]::WriteAllText($outFile, $text, [System.Text.Encoding]::UTF8^)
echo Write-Host "  Done." -ForegroundColor Green
echo Write-Host ""
echo Write-Host $text
) > "%TEMP_PS1%"

:: ── Run the PowerShell script ─────────────────────────────────────
powershell -NoProfile -ExecutionPolicy Bypass -File "%TEMP_PS1%"

if errorlevel 1 (
    echo.
    echo  [ERROR] Something went wrong. Check your API key and input file.
    echo.
    del "%TEMP_PS1%" 2>nul
    exit /b 1
)

echo.
echo  Output saved to: %OUTPUT_FILE%
echo.

:: ── Cleanup ───────────────────────────────────────────────────────
del "%TEMP_PS1%" 2>nul

endlocal
