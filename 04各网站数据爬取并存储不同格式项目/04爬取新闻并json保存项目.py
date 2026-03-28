import json

import requests
import re

url="https://channel.chinanews.com.cn/cns/cl/fz-ffcl.shtml?pager=0"
headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"}
res=requests.get(url,headers=headers)
m=re.search("var docArr=(.*);",res.text).group(1)
dic_items=json.loads(m)
content=[]
for item in dic_items:
    content.append(
        {
            "title":item["title"],
            "url":item["url"],
            "text":item["content"],
            "date":item['pubtime']
        }
    )

with open("反腐新闻网.json","w",encoding="utf-8")as f:
    json.dump(content,f,indent=4,ensure_ascii=False)
print("ok")