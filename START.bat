@echo off
title HELIX DEV STARTER

echo Starting HELIX Development Environment...

:: =========================
:: KILL OLD PROCESSES
:: =========================

taskkill /F /IM electron.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM ollama.exe >nul 2>&1

:: =========================
:: START OLLAMA
:: =========================

start "OLLAMA" cmd /k ollama serve

timeout /t 5 >nul

:: =========================
:: START BACKEND
:: =========================

cd /d "E:\Helix"

start "UVICORN" cmd /k uvicorn api.server:app --reload --host 127.0.0.1 --port 8000

timeout /t 3 >nul

:: =========================
:: START FRONTEND
:: =========================

cd /d "E:\Helix\ui\helix-dashboard"

start "HELIX UI" cmd /k npm run dev

exit