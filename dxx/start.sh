#! /bin/bash

service cron start

nohup python3 -m http.server 80 --directory img > /dev/null 2>&1 &

nohup python3 listen.py > DxxLog/sendImg.log 2>&1 &

python3 app.py
