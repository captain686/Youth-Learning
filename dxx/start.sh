#! /bin/bash

if [ ! -d "img" ]; then
  mkdir img
fi

service cron start

python3 app.py
