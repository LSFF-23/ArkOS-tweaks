@echo off
echo Looking for files in: %cd%
for /R %%i in (*.cue *.gdi *.iso) do (
    echo Found: "%%~nxi"
    chdman createcd -i "%%i" -o "%%~ni.chd"
)
echo Finished.