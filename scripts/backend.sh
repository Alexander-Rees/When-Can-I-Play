#!/bin/bash

os_type=$(uname)

cd backend/db
sqlite3 when_can_i_play.db < init.sql

cd ../flask-app

if [ "$os_type" == "Darwin" ]; then
  python3 -m venv venv
  source venv/bin/activate
elif [ "$os_type" == "Linux" ]; then
  python3 -m venv venv
  source venv/bin/activate
elif [ "$os_type" == "MINGW64_NT-10.0" ]; then
  python -m venv venv
  source venv/Scripts/activate
fi

cd src
pip install --no-cache-dir -r requirements.txt

cd ..
python app.py

deactivate
