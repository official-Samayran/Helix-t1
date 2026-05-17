@echo off
title HELIX MASTER KILLER

echo Killing HELIX...

taskkill /F /IM electron.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM ollama.exe >nul 2>&1

echo HELIX stopped.

timeout /t 2 >nul

exit