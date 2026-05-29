@echo off
echo ============================================
echo   Dogtor v3.0 - 博士生生存模拟器 打包脚本
echo ============================================
echo.

cd /d "%~dp0"

echo [1/3] 清理旧的构建文件...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del /q "*.spec"

echo [2/3] 验证必需文件...
if not exist "simhei.ttf" (
    echo [错误] simhei.ttf 字体文件不存在！
    pause
    exit /b 1
)
if not exist "story_data.py" (
    echo [错误] story_data.py 不存在！
    pause
    exit /b 1
)
echo 所有必需文件检查通过。

echo [3/3] 开始打包...
pyinstaller --onefile --windowed --name "Dogtor" ^
    --add-data "config.py;." ^
    --add-data "story_data.py;." ^
    --add-data "simhei.ttf;." ^
    --hidden-import pygame ^
    --hidden-import config ^
    --hidden-import story_data ^
    --noconfirm ^
    --clean ^
    main.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [错误] 打包失败！
    pause
    exit /b 1
)

echo.
echo ============================================
echo   打包完成！exe 文件位于 dist\Dogtor.exe
echo ============================================
pause
