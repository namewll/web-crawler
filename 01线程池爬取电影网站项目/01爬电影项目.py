import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import pandas as pd

titles = []
move_types = []
places = []
chas = []
times = []
scores = []
srcs=[]
def get_html(page):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url=f"https://ssr1.scrape.center/page/{page}"
    response = requests.get(url, headers=headers)
    obj=BeautifulSoup(response.text, "html.parser")
    divs=obj.find_all("div",class_="el-card item m-t is-hover-shadow")
    for div in divs:
        title=div.find("h2").text.strip().replace("\n",'')
        move_type=div.find("div",class_="categories").text.strip().replace("\n",'')
        place=div.find("div",class_="m-v-sm info").find_all("span")[0].text.strip().replace("\n",'')
        cha=div.find("div",class_="m-v-sm info").find_all("span")[2].text.strip().replace("\n",'')
        time_=div.find_all("div",class_="m-v-sm info")[1].text.strip().replace("\n",'')
        score=div.find('p',class_="score m-t-md m-b-n-sm").text.strip().replace("\n",'')
        src=div.find("img",class_="cover")['src']
        titles.append(title)
        move_types.append(move_type)
        places.append(place)
        chas.append(cha)
        times.append(time_)
        scores.append(score)
        srcs.append(src)
    return {
        "电影名":titles,
        "类型":move_types,
        "地点":places,
        "时长":chas,
        "上映时间":times,
        "评分":scores,
        "图片链接":srcs
    }
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3)as executor:
        result=executor.map(get_html, range(1,8))
        # print(len(list(result)[0]["电影名"]))
    pd.DataFrame(list(result)[0]).to_csv("电影爬虫.csv",encoding="utf-8-sig",index=False)
    print("ok")