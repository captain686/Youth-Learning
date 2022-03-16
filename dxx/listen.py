"""
机器人信息处理
"""

from aiocqhttp import CQHttp, Message
from login import QnDxx
import os
import config
import platform
import threading

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
    
def startBot():
    bot.run(host='127.0.0.1', port=8080)


def finshTask():
    import finsh
    try:
        import schedule
    except:
        os.popen("pip install schedule")
        import schedule
    schedule.every().monday.at("13:00").do(finsh.passInfo)
    schedule.run_all()
    while True:
        schedule.run_pending()


if __name__ =="__main__":
    startbot = threading.Thread(target=startBot)
    if platform.system().lower() == 'windows':
        finshtask = threading.Thread(target=finshTask)
        finshtask.start()
        print(platform.system())
    startbot.start()
    startbot.join()