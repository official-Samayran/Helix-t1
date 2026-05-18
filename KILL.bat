@echo off
title HELIX KILLER

echo Stopping HELIX...

taskkill /F /IM electron.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM ollama.exe >nul 2>&1

echo.
echo HELIX stopped successfully.

timeout /t 2 >nul

exit