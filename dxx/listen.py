"""
机器人信息处理
"""

from aiocqhttp import CQHttp, Message
from login import QnDxx
import os
import config

bot = CQHttp()

def getImg():
    print("获取本地图片中...")
    status = QnDxx().logIn()
    if status:
        return True
    getImg()
     

@bot.on_message('private')
async def handle_msg(event):
    msg = Message(event.message)
    keyword = config.Keyword
    if keyword in str(msg):
        getImg()
        basePath = os.path.dirname(__file__)
        img = os.path.join(basePath,"img","end.png")
        await bot.send(event, f"[CQ:image,cache=0,file=file:///{img}]")
    # imageFile.close()
    

if __name__ =="__main__":
    bot.run(host='127.0.0.1', port=8080)