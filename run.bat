@echo off
setlocal enabledelayedexpansion

:: ====================================================
:: 1. AUTOMATICALLY REQUEST ADMINISTRATOR PRIVILEGES
:: ====================================================
net session >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [INFO] Requesting Administrator rights to ensure Python can install...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Change directory to where this batch file lives (crucial for admin mode)
cd /d "%~dp0"

echo ====================================================
echo Checking System Prerequisites...
echo ====================================================

:: 2. CHECK IF PYTHON IS INSTALLED
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [WARNING] Python is not found on this system.
    echo Attempting to install Python via Windows Package Manager...
    echo.
    
    :: Install Python 3 cleanly using winget
    winget install --id Python.Python.3 --silent --accept-source-agreements --accept-package-agreements
    
    if !ERRORLEVEL! neq 0 (
        echo [ERROR] Failed to install Python automatically. 
        echo Please install it manually from https://www.python.org
        pause
        exit /b
    )
    
    echo [SUCCESS] Python installed successfully!
    echo.
    
    :: Refresh the environment path locally inside this file
    call :refresh_path
) else (
    echo [OK] Python is already installed.
)

:: 3. BUILD OR ACTIVATE VIRTUAL ENVIRONMENT
if not exist .venv (
    echo ====================================================
    echo First-time setup detected. Building environment...
    echo ====================================================
    
    python -m venv .venv
    call .venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    
    if exist requirements.txt (
        pip install -r requirements.txt
    ) else (
        echo [WARNING] requirements.txt not found. Skipping package install.
    )
    
    echo Setup complete!
    echo ====================================================
    echo.
) else (
    call .venv\Scripts\activate.bat
)

:: 4. RUN YOUR APPLICATION
echo Starting application...
if exist main.py (
    python main.py
) else (
    echo [ERROR] Could not find main.py to run.
)

pause
exit /b

:: Registry tool path helper
:refresh_path
for /f "tokens=2*" %%a in ('reg query "HKLM\System\CurrentControlSet\Control\Session Manager\Environment" /v Path 2^>nul') do set "SYS_PATH=%%b"
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path 2^>nul') do set "USER_PATH=%%b"
set "PATH=%SYS_PATH%;%USER_PATH%"
goto :eof
