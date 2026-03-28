import time
import requests
import json
import hashlib

for i in range(1,5):
    data = {
        "keyword": "",
        "provinceNames": [],
        "natureTypes": [],
        "eduLevel": "",
        "categories": [],
        "features": [],
        "pageIndex": i,
        "pageSize": 20,
        "sort": 11
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://pv4y-pc.youzy.cn",
        "Referer": "https://pv4y-pc.youzy.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
        "agent": "objectId:;provinceId:;provinceCode:;userPermissionId:;score:0;",
        "deviceId": "56be39031e9a74b22c838cbb88aeb26a",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "u-sign": "f6a8052b16fbe01064e4c4e86441a642",
        "u-token;": ""
    }
    a=(json.dumps(data)+"&9SASji5OWnG41iRKiSvTJHlXHmRySRp1").lower().replace(" ",'')
    md5_enc=hashlib.md5()
    md5_enc.update(a.encode())
    headers["u-sign"]=md5_enc.hexdigest()

    url = "https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query"
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    print(f"第{i}页")
    print(response.text)
    time.sleep(1)
