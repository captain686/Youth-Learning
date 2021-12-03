"""
机器人信息处理
    用于处理机器人接受到的信息，并返回信息
    因为CQHttp好像只支持发送图片的url，所以本地会启动一个80端口的http服务
        即 imgUrl 参数
"""

from aiocqhttp import CQHttp, MessageSegment, Message
from login import QnDxx
import os
import config

bot = CQHttp()

def getImg():
    print("获取本地图片中...")
    try:
        QnDxx().logIn()
    except:
        print("[!] Error ...")
        os.popen("ps -elf|grep chrome |awk '{print $4}'|xargs kill -9")
        getImg()
     

@bot.on_message('private')
async def handle_msg(event):
    msg = Message(event.message)
    keyword = config.Keyword
    if keyword in str(msg):
        getImg()
        imgUrl = "http://127.0.0.1/end.png"
        img = MessageSegment.image(imgUrl)
        await bot.send(event, img)
    # imageFile.close()
    

if __name__ =="__main__":
    bot.run(host='127.0.0.1', port=8080)