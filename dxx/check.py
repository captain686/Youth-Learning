import requests
import config


# 获取代理
def get_proxy():
    print("Get Proxy...")
    return requests.get(f"http://{config.proxyPool_url}:5010/get/").json()


# 删除无效代理
def delete_proxy(proxy):
    print("Delete {}".format(proxy))
    requests.get("http://proxy_pool:5010/delete/?proxy={}".format(proxy))

# your spider code
# 验证代理
def checkProxy():
    # ....
    proxyInfo = get_proxy()
    # retry_count = 5
    proxy = proxyInfo.get("proxy")
    # while retry_count > 0:
    try:
        print(f"[*] Check Proxy {proxy}")
        html = requests.get('http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=getNewestVersionInfo', proxies={"http": "http://{}".format(proxy),"https": "https://{}".format(proxy)},timeout=5)
        # 使用代理访问
        print(html.status_code)
        if html.status_code == 200:
            return proxy
        else:
            checkProxy()
    except Exception:
        delete_proxy(proxy)
        checkProxy()      
    # 删除代理池中代理
    # return None
