# encoding:utf-8
import subprocess
from functools import partial
from bs4 import BeautifulSoup
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import time
import requests
import json
import execjs
import os
from concurrent.futures import ThreadPoolExecutor
def get_html(item):
    try:
        kind=item["KIND"]
        m_id=item["M_ID"]
        name=item["NAME"]
        url = "https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfoDetail"
        data = {
            "ts": int(time.time()*1000),
            "name": name,
            "cid": f"{m_id}",
            "type": kind
        }
        headers["portal-sign"]=execjs.compile(code1).call("d",data)
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        encrypt_text1=response.json()["Data"]
        first_text1 = execjs.compile(code1).call('b', encrypt_text1)
        value=json.loads(first_text1)["BaseInfo"]

        title=value["NOTICE_NAME"]
        sell_date=value["DOC_GET_END_TIME"]
        prove_money_end_time=value["M_ZY_TM"]
        what_end_time=value["M_BZJ_TM"]
        invest_end_time=value["BID_DOC_REFER_END_TIME"]
        tb_number=value["TENDER_PROJECT_CODE"]
        change_plat=value["PLATFORM_CODE_NAME"]
        print(title)

        url = "https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfoContent"
        data = {
            "type": 1,
            "m_id": f"{m_id}",
            "ts": int(time.time()*1000)
        }
        headers["portal-sign"]=execjs.compile(code1).call("d",data)
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        encrypt_text1=response.json()["Data"]
        first_text1 = execjs.compile(code1).call('b', encrypt_text1)
        notice_content=json.loads(first_text1)
        # print(notice_content['Contents'])
        soup=BeautifulSoup(notice_content['Contents'],"html.parser")
        ps=soup.find_all("p")
        for p in ps:
            passage.append(p.text)
        last_content="\n".join(passage)
        path=f"./福建省资源平台/{title}.txt"
        with open(path,"w",encoding="utf-8") as f:
            f.write(f"标题：{title}\n")
            f.write(f"标书售卖截止时间：{sell_date}\n")
            f.write(f"保证金缴纳截止时间：{prove_money_end_time}\n")
            f.write(f"质疑截止时间：{what_end_time}\n")
            f.write(f"投标截止时间：{invest_end_time}\n")
            f.write(f"招标编号：{tb_number}\n")
            f.write(f"交易平台：{change_plat}\n")
            f.write(f"公告内容：{last_content}")
    except:
        print("wwwwwwwwwwwwwwwwwwww")

if __name__=="__main__":

    with open("14zuoye.js", "r", encoding="utf-8") as f:
        code1 = f.read()

    if not os.path.exists("./福建省资源平台"):
        os.makedirs("./福建省资源平台")
    passage = []
    for page in range(1, 5):
        print(page)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://ggzyfw.fj.gov.cn",
            "Referer": "https://ggzyfw.fj.gov.cn/business/list/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "portal-sign": "bba9c967943e8fa2b7401ba9a9292901",
            "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\""
        }
        cookies = {
            "ASP.NET_SessionId": "d34cn11jws405cxtvd4mvgz4"
        }
        url = "https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo"
        data = {
            "ts": int(time.time() * 1000),
            "pageNo": page,
            "pageSize": 20,
            "total": 3321,
            "KIND": "GCJS",
            "GGTYPE": "1",
            "timeType": "1",
            "BeginTime": "2025-08-10 00:00:00",
            "EndTime": "2026-02-10 23:59:59",
            "createTime": [],
        }
        if page > 1:
            data["total"] = 3317
        headers["portal-sign"] = execjs.compile(code1).call("d", data)
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        encrypt_text = response.json()["Data"]
        first_text = execjs.compile(code1).call('b', encrypt_text)
        items = json.loads(first_text)["Table"]
        with ThreadPoolExecutor(max_workers=5)as executor:
            executor.map(get_html,items)









