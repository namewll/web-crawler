# encoding:utf-8
import json
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import requests
import execjs
import pandas as pd

index_=0
new_content=[]
for page in range(1,5):
    with open("13guanniao参数.js", "r", encoding="utf-8") as f:
        code=f.read()
    data1=f'page={page}&limit=20'
    result_list=execjs.compile(code).call("main",data1)
    with open("13guanniao结果.js", "r", encoding="utf-8") as f:
        code1=f.read()

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.birdreport.cn",
        "Referer": "https://www.birdreport.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
        "requestId": str(result_list[0]),
        "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sign": str(result_list[1]),
        "timestamp": str(result_list[2])
    }
    url = "https://api.birdreport.cn/front/activity/search"
    response = requests.post(url, headers=headers, data=result_list[-1])
    content=response.json()["data"]
    detail_content=execjs.compile(code1).call("decode",content)
    items=json.loads(detail_content)
    for item in items:
        index_+=1
        address=item["address"]
        pointName=item["pointName"]
        startTime=item["startTime"]
        endTime=item["endTime"]
        username=item["username"]
        taxonCount=item["taxonCount"]
        visitsCount=item["visitsCount"]
        new_content.append({
            "序号":index_,
            "目标":pointName,
            "开始时间":startTime,
            "结束时间":endTime,
            "观测地点":address,
            "记录用户":username,
            "鸟种数量":taxonCount,
            "浏览数":visitsCount
        })
pd.DataFrame(new_content).to_excel("中国观鸟.xlsx",index=False)
print("ok")
