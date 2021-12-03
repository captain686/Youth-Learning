"""
主要截图文件

openid注入链接
https://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=

添加localStorage
window.localStorage.setItem("openid",f"config.openid");
获取localStorage
window.localStorage.getItem("openid");
"""
from typing import runtime_checkable
from pic import Pic
import time, sys
from selenium import webdriver
import config
from rich.console import Console
console = Console()
from check import checkProxy


class QnDxx(Pic):
    def __init__(self):
        self.proxy = checkProxy()
        chrome_option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        chrome_option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        chrome_option.add_argument('--headless')
        chrome_option.add_argument('--no-sandbox')
        chrome_option.add_argument(f'--proxy-server={self.proxy}')
        # chrome_option.add_argument('--disable-javascript')
        # chrome_option.add_argument('--headless')
        chrome_option.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x18001031) NetType/WIFI Language/zh_CN')
        mobileEmulation = {'deviceName': 'iPhone X'}
        chrome_option.add_experimental_option('mobileEmulation', mobileEmulation)
        # chrome_option.add_argument("--auto-open-devtools-for-tabs")
        # chrome_option.add_extension("quick-javascript-switcher.crx")
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.set_page_load_timeout(10)
        self.driver.set_script_timeout(10)
        self.driver.set_window_size(376,1493)
        self.driver.get("chrome://newtab")

    
    # 添加openid，登陆平台
    def logIn(self):
        self.driver.get("chrome://settings/cookies")
        time.sleep(2)
        self.driver.get_screenshot_as_file("img/111.png")
        self.driver.get("http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=getNewestVersionInfo")
        time.sleep(2)
        console.print("[+] 注入openid ...",style="bold green",end='\r')
        self.driver.execute_script(f'localStorage.setItem("openid","{config.openid}");')
        time.sleep(0.5)

        self.driver.get("http://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=")

        console.print("[-] Refresh ...",style="bold yellow",end='\r')

        now_url = self.driver.current_url
        if "open.weixin.qq.com" in now_url:
            console.print("[!] openid注入失败",style="bold red")
        self.getXxjldetail()
        
        
    # 截取积分记录&学习记录页面图片
    def getXxjldetail(self):
        path = super().allPath()+"/img/"
        self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[3]').click()
        self.driver.find_element_by_xpath('//*[@id="my"]/div[1]/div[2]/div[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body').screenshot(path+"one.png")
        self.driver.refresh()
        console.print("[*] Refresh ...",style="bold yellow")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[3]').click()
        self.driver.find_element_by_xpath('//*[@id="my"]/div[1]/div[2]/div[3]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body').screenshot(path+"two.png")
        # time.sleep(50)
        self.quit()
        Pic().getPic()


    def quit(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    QnDxx().logIn()
    