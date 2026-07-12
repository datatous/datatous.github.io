@echo off
REM datatous 관리자 편집 저장 서버 런처 (더블클릭 실행)
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0.."
echo repo: %CD%
python tools\admin_edit_server.py %*
pause
