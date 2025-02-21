@echo off
echo Fixing psycopg2 installation...
call venv\Scripts\activate
pip install --upgrade pip
pip install psycopg2 psycopg2-binary
echo psycopg2 installation completed.
pause
