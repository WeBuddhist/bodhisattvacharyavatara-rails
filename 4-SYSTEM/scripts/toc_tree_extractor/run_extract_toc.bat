@echo off
REM ============================================================
REM  Launcher for extract_toc_tree.py
REM  Double-click to run. Your API key is typed in at runtime
REM  and is NOT stored in this file.
REM ============================================================
chcp 65001 >nul
setlocal
cd /d "%~dp0"

REM --- ask for the API key FIRST (not echoed to a file) ---
:askkey
set "GEMINI_API_KEY="
set /p "GEMINI_API_KEY=Paste your Gemini API key, then press Enter: "
if not defined GEMINI_API_KEY (
    echo No key entered. Please try again.
    goto askkey
)

REM --- ask for the input file path (drag the file in, or paste its path) ---
:askinput
set "INPUT="
set /p "INPUT=Enter the path to the commentary file (.md/.txt): "
REM strip any quotes the user/drag-drop may have added
set INPUT=%INPUT:"=%
if not defined INPUT (
    echo No path entered. Please try again.
    goto askinput
)
if not exist "%INPUT%" (
    echo File not found: %INPUT%
    echo Please try again.
    goto askinput
)
echo Input file: %INPUT%

REM --- check Python ---
where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python was not found on PATH.
    echo Install Python 3 from https://www.python.org/downloads/ and try again.
    pause
    exit /b 1
)

REM --- ensure dependencies are installed ---
python -c "import google.genai" >nul 2>&1
if errorlevel 1 (
    echo Installing google-genai ...
    python -m pip install --quiet google-genai
)

REM --- syntax-check the script before running ---
python -m py_compile extract_toc_tree.py
if errorlevel 1 (
    echo [ERROR] extract_toc_tree.py has a syntax error.
    pause
    exit /b 1
)

REM --- run the pipeline (Pass 1 candidates, Pass 2 enumerations, then TOC tree + QC) ---
echo.
echo Running extraction on "%INPUT%" ...
python extract_toc_tree.py "%INPUT%"
set "RC=%ERRORLEVEL%"

echo.
if "%RC%"=="0" (
    echo Done. Outputs in 0-INBOX\:
    echo   - toc-candidates-^<id^>.md              ^(section candidates^)
    echo   - toc-tree-^<id^>.md                    ^(nested TOC tree^)
    echo   - toc-tree-qc-^<id^>.md                 ^(QC report^)
    echo   - temp\TOC-^<id^>\enumerations\         ^(one raw enumeration file per chunk^)
) else (
    echo [FINISHED WITH ERRORS] exit code %RC%. Re-run to resume from where it stopped.
)
echo.
pause
endlocal
