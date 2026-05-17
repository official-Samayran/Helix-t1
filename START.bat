@echo off
title HELIX MASTER STARTER

echo Starting HELIX...

:: =========================
:: KILL OLD PROCESSES
:: =========================

taskkill /F /IM electron.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1

:: =========================
:: START OLLAMA
:: =========================

start "" /MIN cmd /c ollama serve

timeout /t 5 >nul

:: =========================
:: START FASTAPI BACKEND
:: =========================

cd /d "E:\Helix"

start "" /MIN cmd /c uvicorn api.server:app --host 127.0.0.1 --port 8000

timeout /t 5 >nul

:: =========================
:: START FRONTEND
:: =========================

cd /d "E:\Helix\ui\helix-dashboard"

start "" /MIN cmd /c npm run dev

exit