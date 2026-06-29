@echo off
REM ============================================================
REM  Launcher for generate_practice_plan.py
REM  Double-click to run, or call from the vault root.
REM  Your API key is entered at runtime and NOT stored here.
REM ============================================================
chcp 65001 >nul
setlocal
cd /d "%~dp0"

REM --- ask for the API key ---
:askkey
set "GEMINI_API_KEY="
set /p "GEMINI_API_KEY=Paste your Gemini API key, then press Enter: "
if not defined GEMINI_API_KEY (
    echo No key entered. Please try again.
    goto askkey
)

REM --- ask for the day number ---
:askday
set "DAY="
set /p "DAY=Enter the day number (1-365): "
if not defined DAY (
    echo No day entered. Please try again.
    goto askday
)

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
python -m py_compile generate_practice_plan.py
if errorlevel 1 (
    echo [ERROR] generate_practice_plan.py has a syntax error.
    pause
    exit /b 1
)

REM --- run the generator ---
echo.
echo Generating practice plan for Day %DAY% ...
python generate_practice_plan.py %DAY%
set "RC=%ERRORLEVEL%"

echo.
if "%RC%"=="0" (
    echo Done. The file has been written to 3-TRANSFORMATIONS\Plans\the-bodhisattva-challenge\bo\
) else (
    echo [FINISHED WITH ERRORS] exit code %RC%.
)
echo.
pause
endlocal
