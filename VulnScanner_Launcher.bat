@echo off
cd /d E:\tool
start "" "dist\VulnScanner.exe"
timeout /t 3 /nobreak >nul
start http://127.0.0.1:5000
exit