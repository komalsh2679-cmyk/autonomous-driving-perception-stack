@echo off
setlocal
cd /d "%~dp0"
if exist .venv\Scripts\activate.bat call .venv\Scripts\activate.bat
python -m src.main --config config/settings.yaml
if errorlevel 1 (
  echo.
  echo The demo exited with an error. Read the message above.
  pause
)
