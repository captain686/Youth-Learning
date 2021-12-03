"""
获取视频结尾完成图
"""
# from concurrent.futures import ThreadPoolExecutor
# import threading
from flask import Flask, url_for, render_template
from flask import jsonify
import requests
requests.packages.urllib3.disable_warnings()


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

img_dict = {'img_url': None}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303004c)',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}


# def find_url(start, end):
#     for id in range(start, end):
#         url = f"https://h5.cyol.com/special/daxuexi/af7ina30ly/images/end/{id}.jpg"
#         if requests.get(url, headers).status_code != 200:
#             return id-1
#     return ""


# 获取最新一期视频链接
def get_url():
    json_url = "https://h5.cyol.com/special/weixin/sign.json"
    date = requests.get(json_url,headers).json()
    for k, v in date.items():
        raw = v
    url = raw.get("url")
    if url:
        return url
    return ""


# 特别期的图片名不确定，通过Fuzz获取图片
def fuzzPic(id):
    img_url = get_url()
    video_name = img_url.split('/')[-1]
    img = img_url.replace(video_name, "images/end/")
    fin_url = f"{img}/{id}.jpg"
    res = requests.get(fin_url,headers=headers)
    if res.status_code != 200:
        return f"{img}/{id-1}.jpg"
    return ""

# 返回图片链接
@app.route('/')
def get_image():
    img_url = get_url()
    if img_url:
        video_name = img_url.split('/')[-1]
        img = img_url.replace(video_name, "images/end.jpg")
        res = requests.get(img, headers)
        # print(res.status_code, res.raw)
        if res.status_code == 200:
            img_dict.update({'img_url': img})
            return jsonify(img_dict)
        else:
            id = 1
            while True:
                status = fuzzPic(id)
                if status:
                    return jsonify({'img_url': f'{status}'})
                id += 1
    else:
        return jsonify(img_dict)


# 返回图片
@app.route('/img/')
def img():
    img_url = get_url()
    if img_url:
        video_name = img_url.split('/')[-1]
        img = img_url.replace(video_name, "images/end.jpg")
        # img = img_url+"/.."
        if requests.get(img, headers).status_code == 200:
            return render_template("img.html", img=img)
        else:
            id = 1
            while True:
                status = fuzzPic(id)
                if status:
                    return render_template("img.html", img=status)
                id += 1      
    else:
        return jsonify(img_dict)
        
        
if __name__ == '__main__':
    print(get_url())
    # app.run(host="0.0.0.0")
    