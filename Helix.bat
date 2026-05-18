@echo off
title HELIX Launcher

echo Starting HELIX...

:: =========================
:: KILL OLD HELIX PROCESSES
:: =========================

taskkill /F /IM electron.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM ollama.exe >nul 2>&1

:: =========================
:: START OLLAMA
:: =========================

start "OLLAMA" /MIN cmd /k ollama serve

timeout /t 5 >nul

:: =========================
:: START FASTAPI BACKEND
:: =========================

cd /d "E:\Helix"

start "UVICORN" /MIN cmd /k uvicorn api.server:app --host 127.0.0.1 --port 8000

timeout /t 3 >nul

:: =========================
:: START FRONTEND + ELECTRON
:: =========================

cd /d "E:\Helix\ui\helix-dashboard"

start "HELIX UI" cmd /k npm run dev

exit