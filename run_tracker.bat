@echo off
:: Taiwan Earthquake Tracker Quick Launcher for Windows
:: Sets up a console menu to easily run the earthquake tracker tool

chcp 65001 > nul
set LOCAL_PATH=%~dp0
cd /d %LOCAL_PATH%

:menu
cls
echo ==================================================
echo         台灣地震追蹤器 (Taiwan Earthquake Tracker)
echo ==================================================
echo.
echo   [1] 抓取最新地震資料 (Fetch Earthquake Data)
echo   [2] 啟動地震儀表板 (Launch Earthquake Dashboard)
echo   [3] 抓取並啟動儀表板 (Fetch and Launch)
echo   [4] 結束 (Exit)
echo.
echo ==================================================
set /p choice="請輸入選項 [1-4]: "

if "%choice%"=="1" goto fetch
if "%choice%"=="2" goto serve
if "%choice%"=="3" goto both
if "%choice%"=="4" goto exit
goto menu

:fetch
echo.
echo [*] 正在抓取最新地震資料...
python earthquake_tracker.py --fetch
echo.
echo [+][完成] 地震資料已抓取並儲存在 data/ 目錄下。
pause
goto menu

:serve
echo.
echo [*] 正在啟動儀表板伺服器...
python earthquake_tracker.py --serve
goto menu

:both
echo.
echo [*] 正在抓取最新地震資料...
python earthquake_tracker.py --fetch
echo [*] 正在啟動儀表板伺服器...
python earthquake_tracker.py --serve
goto menu

:exit
echo.
echo 感謝使用台灣地震追蹤器！再見！
timeout /t 2 > nul
exit
