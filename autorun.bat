@echo off

echo Creating your playlist...
cd scripts
python dailymotion_m3ugrabber.py > ../playlist.m3u8

pause
