@echo off
echo =========================================
echo  Yashwini Shetty - CV Website
echo =========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask server...
echo Website will be available at: http://localhost:5001
echo.
python app.py
pause
