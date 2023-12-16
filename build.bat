cd /d D:\A-Project\Python-project\super-worker-bee\.venv\Scripts

ping -n 1 127.0>nul
call activate.bat

ping -n 1 127.0>nul
cd /d D:\A-Project\Python-project\super-worker-Bee

ping -n 1 127.0>nul
call Pyinstaller -F -w -i favicon.ico -n WorkerBee main.py

ping -n 4 127.0>nul
copy favicon.ico dist

ping -n 1 127.0>nul
cmd /k "del /f /q WorkerBee.spec && rd /s /q D:\A-Project\Python-project\super-worker-bee\build"

