@echo off
setlocal

set "GIT_NAME=Liangzhenkun"
set "GIT_EMAIL=113508178+Liangzhenkun@users.noreply.github.com"

echo.
echo == Git Bootstrap for Windows ==
echo This script will set your global Git identity on this computer.
echo.

where git >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Git is not installed or not on PATH.
  exit /b 1
)

git config --global user.name "%GIT_NAME%"
if errorlevel 1 (
  echo [ERROR] Failed to set global user.name.
  exit /b 1
)

git config --global user.email "%GIT_EMAIL%"
if errorlevel 1 (
  echo [ERROR] Failed to set global user.email.
  exit /b 1
)

git config --global init.defaultBranch main
if errorlevel 1 (
  echo [ERROR] Failed to set init.defaultBranch.
  exit /b 1
)

echo.
echo Global Git configuration on this computer is now:
echo   user.name  = %GIT_NAME%
echo   user.email = %GIT_EMAIL%
echo   init.defaultBranch = main
echo.

echo Verifying:
git config --global --get user.name
git config --global --get user.email
git config --global --get init.defaultBranch

if exist ".git" (
  if exist "scripts\install_git_hooks.ps1" (
    echo.
    echo Repository detected. Installing local hooks for this repo...
    powershell -NoProfile -ExecutionPolicy Bypass -File ".\scripts\install_git_hooks.ps1"
  )
)

echo.
echo Done.
echo On a new computer, run this file once after Git is installed.
exit /b 0
