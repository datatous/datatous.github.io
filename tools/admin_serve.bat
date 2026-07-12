@echo off
REM datatous 관리자 편집 저장 서버 런처 (더블클릭 실행)
REM 작동하는 Python 인터프리터를 자동 탐색한다 (WindowsApps 스토어 스텁 회피).
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0.."
echo repo: %CD%

set "PYEXE="

REM 1) 후보들을 순서대로 "실제 파이썬인지" 검사
for %%P in (
  "%LOCALAPPDATA%\hermes\hermes-agent\venv\Scripts\python.exe"
  "py -3"
  "python"
  "python3"
) do (
  if not defined PYEXE (
    %%~P -c "import sys" >nul 2>&1 && set "PYEXE=%%~P"
  )
)

if not defined PYEXE (
  echo.
  echo [오류] 작동하는 Python 3 을 찾지 못했습니다.
  echo   - python.org 에서 Python 설치 후 다시 실행하거나
  echo   - 실제 python.exe 전체 경로로 직접 실행하세요:
  echo       ^<python.exe 경로^> tools\admin_edit_server.py
  echo.
  pause
  exit /b 1
)

echo python: %PYEXE%
%PYEXE% tools\admin_edit_server.py %*
pause
