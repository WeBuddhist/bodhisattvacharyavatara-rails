@echo off
cd /d "%~dp0"
echo Running 365-day study plan generator...
python generate_spyod_jug_plan.py
if errorlevel 1 (
    echo.
    echo ERROR: Python script failed. Make sure Python 3 is installed.
    echo Try: python3 generate_spyod_jug_plan.py
    python3 generate_spyod_jug_plan.py
)
echo.
pause
