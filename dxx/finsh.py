# -*- coding: UTF-8 -*-
import requests
import config


requests.packages.urllib3.disable_warnings()


def getNewestVersionInfo():
    url = "http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=getNewestVersionInfo"

    headers = {
        "Origin": "http://qndxx.youth54.cn",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x18001031) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=",
        "Host": "qndxx.youth54.cn",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Content-Length": "0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=5)
        print(f"getNewestVersionInfo Status {response.status_code}")
        if response.status_code == 200:
            version = response.json()
            return version["version"]
        return ""
    except:
        return ""


def passInfo():
    url = "http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=studyLatest"
    headers = {
        "Origin": "http://qndxx.youth54.cn",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Referer": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=enterIndexPage&fxopenid=&fxversion=",
        "Connection": "close",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Site": "same-origin",
        "Host": "qndxx.youth54.cn",
        "Accept-Encoding": "gzip, deflate",
        "Dnt": "1",
        "Sec-Fetch-Mode": "cors",
        "Te": "trailers",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Length": "48",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    version = getNewestVersionInfo()

    if version:
        # sys.exit(0)
        # version = "12-a"
        data = f"openid={config.openid}&version={version}"
        try:
            response = requests.post(url, data=data, headers=headers, verify=False,
                                     timeout=5)

            print(response.status_code, response.json())

            if response.status_code == 200 and response.json()["errcode"] == "0":
                print("[*] Success ")
        except Exception as e:
            print(e)
    else:
        print("[!] Error !!!")


if __name__ == "__main__":
    passInfo()
