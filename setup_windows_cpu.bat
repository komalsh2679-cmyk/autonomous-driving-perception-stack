@echo off
setlocal
cd /d "%~dp0"
echo === Autonomous Driving project: Windows CPU setup ===
where python >nul 2>nul
if errorlevel 1 (
  echo Python was not found. Install Python 3.10 or 3.11 and enable "Add Python to PATH".
  pause
  exit /b 1
)
python --version
if not exist .venv\Scripts\python.exe (
  python -m venv .venv
  if errorlevel 1 goto :error
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
if errorlevel 1 goto :error
python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
if errorlevel 1 goto :error
python -m pip install -r requirements.txt
if errorlevel 1 goto :error
echo.
echo Setup complete. Next, double-click run_demo.bat
echo First YOLO run may download model weights and needs an internet connection.
pause
exit /b 0
:error
echo.
echo Setup failed. Read the error above before trying again.
pause
exit /b 1
