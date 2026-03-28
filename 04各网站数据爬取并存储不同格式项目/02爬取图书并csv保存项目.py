import requests
from bs4 import BeautifulSoup
import pandas as pd
for i in range(0,3):
    index=0
    url=f"https://book.douban.com/top250?start={index}"
    index+=25
    headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,"lxml")
    div=soup.find("div",class_="indent")
    trs=div.find_all("tr",class_="item")
    content=[]
    for tr in trs:
        title=tr.find("div",class_="pl2").a.text.strip().replace("\n","").replace(" ","")
        totals=tr.find("p",class_="pl").text
        sp=totals.split("/ ")
        price=sp[-1]
        date=sp[-2]
        public=sp[-3]
        author=sp[:-3][0]
        content.append(
            {
                "书名":title,
                "价钱":price,
                "时间":date,
                "出版社":public,
                "作者":author
            }
        )
    pd.DataFrame(content).to_csv("book.csv",encoding="utf-8-sig",index=False)
print("ok")


