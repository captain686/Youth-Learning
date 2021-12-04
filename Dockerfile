FROM captain686/chrome-selenium

COPY dxx/ home/dxx

WORKDIR /home/dxx

RUN chmod 777 start.sh \
    && mkdir -p /usr/share/fonts/chinese/ \
    && chmod 777 qbot/o-cqhttp \
    && mkdir img

COPY dxx/tff/MI_LanTing_Regular.ttf /usr/share/fonts/chinese/

RUN apt-get update \
    &&apt-get install -y cron \
    && fc-cache /usr/share/fonts/chinese/ \
    && service cron start

RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple &&\
    pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN crontab crontab \
    && rm -rf crontab \
    && rm requirements.txt

CMD ["bash","start.sh"]