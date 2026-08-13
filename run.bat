@echo off
setlocal


if not exist .venv (
    echo ====================================================
    echo First-time setup detected. Building environment...
    echo ====================================================
    
    python -m venv .venv
    
 
    call .venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    
    echo Setup complete!
    echo ====================================================
    echo.
) else (

    call .venv\Scripts\activate.bat
)
echo Starting application...
python main.py

pause