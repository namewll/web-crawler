# encoding:utf-8
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs

headers = {
    "accept": "text/plain, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://search.bidcenter.com.cn",
    "priority": "u=1, i",
    "referer": "https://search.bidcenter.com.cn/",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
url = "https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx"
data = {
    "from": "6137",
    "guid": "643a5787-30d4-4c91-a8f7-af4b0d6e3602",
    "location": "6138",
    "token": "",
    "keywords": "%e5%9b%ad%e6%9e%97+%e7%bb%bf%e5%8c%96",
    "mod": "0"
}
response = requests.post(url, headers=headers, data=data)
with open('12采招网(引用).js', 'r', encoding='utf-8') as f:
    js_code = f.read()
a = execjs.compile(js_code).call('get_data',response.text)
print(a)












