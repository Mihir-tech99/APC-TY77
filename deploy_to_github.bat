@echo off
title Push Cloud Storage Optimizer Updates to GitHub
cd /d "%~dp0"
echo ========================================================
echo   Pushing Cloud Storage Optimizer to GitHub & Vercel
echo ========================================================
echo.
git add app.py drive_service.py optimizer.py UPLOAD_THESE_2_FILES_TO_GITHUB/
git commit -m "Fix SHA-256 duplicate detection, WebCrypto lab hasher, batch trash, and Vercel stateless sync"
git push origin main --force
echo.
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Code pushed successfully to GitHub!
    echo Vercel is now automatically rebuilding and deploying your updated project at:
    echo https://cloud-storage-jqfx.vercel.app/
) else (
    echo [NOTICE] If Git prompted you for credentials, please sign in with your GitHub account.
    echo Alternatively, you can drag and drop the files in the 'UPLOAD_THESE_2_FILES_TO_GITHUB'
    echo folder directly into your repository on github.com/Mihir-tech99/cloud-storage.
)
echo.
pause
