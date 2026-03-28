import requests
from datetime import datetime
import re
import pandas as pd

content = []
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "client-version": "3.0.0",
    "priority": "u=1, i",
    "referer": "https://weibo.com/u/2177142893",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "server-version": "v2026.01.27.1",
    "traceparent": "00-c76d85925f90313a8fe96c2149daea7a-8b3d1d8e97086741-00",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "Gh9KPQ3CQ03xqWFMEkpm7gBM"
}
cookies = {
    "XSRF-TOKEN": "Gh9KPQ3CQ03xqWFMEkpm7gBM",
    "SCF": "AuQVzaI4Lzjk9nEIhBrhwGKcQiArzVPGhv0Hx63aod-6rPOYnc9koC4UfnMNZm5kLDMZd0TzkmTiZ6jt3e6EsyE.",
    "SUB": "_2A25EfCBUDeRhGe5N71MY8CvPwzuIHXVn8D2crDV8PUNbmtANLUfgkW9NdJM0TDfcrSa235W3_UR2pgdpWAESYT-Z",
    "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WhOErvmGH8LN0NM6mOVTIxw5JpX5KzhUgL.Fon0Sh24eh-01hM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMRe0Bp1K5fe0nN",
    "ALF": "02_1772084484",
    "WBPSESS": "zjI2F1gUKLWLTJTs0zbtOKWR6qCWnOx420VmTD79wgOp4dme7LfrMFjBywVUN49_mtvVIXxfR35sUG9olThZAuVDuCZmYabw67C75JRFA9CAeK6LRPb87JL9vN2zWJSCFY6t5suWtET84FIK3u7pLQ=="
}
uid=input("输入你想要查找的明星id:")
for page in range(1,5):
    url = "https://weibo.com/ajax/statuses/mymblog"
    params = {
        "uid": f"{uid}",
        "page": f"{page}",
        "feature": "0",
    }
    res = requests.get(url, headers=headers, cookies=cookies, params=params)
    items=res.json()["data"]["list"]
    user_name = items[0]["user"]["screen_name"]
    since_id=res.json()["data"]["since_id"]
    params["since_id"]=since_id
    for item in items:
        created_at = item.get("created_at","")
        # Sat Sep 06 22:16:06 +0800 2025
        created_time=datetime.strptime(created_at,"%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S")
        place=item.get("region_name","")
        if place:
            place_name=re.findall("发布于 (.*)",place)[0]
        else:
            place_name=place
        text=item.get("text_raw","")
        share=item.get("reposts_count","")
        comment=item.get("comments_count","")
        like=item.get("attitudes_count","")
        content.append({
            "发布时间":created_time,
            "发布地点":place_name,
            "内容":text,
            "分享次数":share,
            "评论次数":comment,
            "点赞次数":like
        })
pd.DataFrame(content).to_excel(f"{user_name}微博.xlsx",index=False)
print("ok")


