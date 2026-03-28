import time

import requests
import json
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/json",
    "cookieorigin": "https://hotels.ctrip.com",
    "origin": "https://hotels.ctrip.com",
    "priority": "u=1, i",
    "referer": "https://hotels.ctrip.com/",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
cookies = {
    "GUID": "09031145414149532436",
    "nfes_isSupportWebP": "1",
    "UBT_VID": "1757246607634.21cdi7IVmiu5",
    "MKT_CKID": "1757246608071.t6n2i.dd6m",
    "_RF1": "60.169.16.37",
    "_RSG": "9eKRPRlgU_8K83Lt8LNKm8",
    "_RDG": "28e09e1f232da8202c1c68bde52eb3fc33",
    "_RGUID": "8fdeaaf6-d96d-4a09-8c14-5d5237543214",
    "_ubtstatus": "%7B%22vid%22%3A%221757246607634.21cdi7IVmiu5%22%2C%22sid%22%3A1%2C%22pvid%22%3A2%2C%22pid%22%3A311002%7D",
    "_bfaStatusPVSend": "1",
    "_bfaStatus": "success",
    "ibulocale": "zh_cn",
    "cookiePricesDisplayed": "CNY",
    "IBU_showtotalamt": "2",
    "_bfa": "1.1757246607634.21cdi7IVmiu5.1.1757246961009.1773565467192.2.1.10650171194",
    "_jzqco": "%7C%7C%7C%7C1773565469905%7C1.187126124.1773565469327.1773565469327.1773565469327.1773565469327.1773565469327.0.0.0.1.1",
    "ibulanguage": "CN"
}
url = "https://m.ctrip.com/restapi/soa2/33278/getHotelCommentList"
content=[]
def parse(page):
    data = {
        "hotelId": 116959562,
        "pageIndex": page,
        "pageSize": 10,
        "repeatComment": 1,
        "needStaticInfo": False,
        "functionOptions": [
            "integratedTopComment",
            "ctripIntegratedExpediaTaList"
        ],
        "head": {
            "platform": "PC",
            "cver": "0",
            "cid": "1757246607634.21cdi7IVmiu5",
            "bu": "HBU",
            "group": "ctrip",
            "aid": "",
            "sid": "",
            "ouid": "",
            "locale": "zh-CN",
            "timezone": "8",
            "currency": "CNY",
            "pageId": "102003",
            "vid": "1757246607634.21cdi7IVmiu5",
            "guid": "",
            "isSSR": False
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    items=response.json()['data']['commentList']
    for item in items:
        name=item['userInfo']['nickName']
        createDate=item['createDate']
        roomTypeName=item['roomTypeName']
        comment=item['content']
        commentLevel=item['commentLevel']
        content.append({
            '来源用户':name,
            '发布时间':createDate,
            '房型':roomTypeName,
            '评论':comment,
            '评价':commentLevel
        })
        print(name)
    time.sleep(1)

if __name__ == '__main__':
    startTime=time.time()
    with ThreadPoolExecutor(max_workers=5)as executor:
        executor.map(parse,range(1,22))
    pd.DataFrame(content).to_excel('牧瑶温泉民宿（忻州古城店）.xlsx', index=False)
    print(time.time()-startTime)

