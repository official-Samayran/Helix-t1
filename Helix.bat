@echo off
title HELIX Launcher

cd /d "E:\Helix"

:: START MAIN.PY MINIMIZED
start "" /MIN cmd /c python "E:\Helix\main.py"

:: START FASTAPI SERVER
start "" /MIN cmd /c uvicorn api.server:app --host 127.0.0.1 --port 8000

cd /d "E:\Helix\ui\helix-dashboard"

start "" /MIN cmd /c npm run dev

exit