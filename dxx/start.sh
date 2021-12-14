#! /bin/bash

service cron start

nohup python3 listen.py > DxxLog/sendImg.log 2>&1 &

python3 app.py
