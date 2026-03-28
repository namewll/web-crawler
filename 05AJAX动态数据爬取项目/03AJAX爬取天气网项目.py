import os.path

import requests
import re
import json
from datetime import datetime
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor



def get_html(city_key,city_value):
    city_id=city_value[city_key]["AREAID"]
    content = []
    date_str=[]
    for i in range(1,13):
        if i<10:
            month="0"+f"{i}"
        else:
            month=f"{i}"
        params["-"]=int(time.time()*1000)
        url = f"https://d1.weather.com.cn/calendar_new/2025/{city_id}_2025{month}.html"
        res = requests.get(url, headers=headers, cookies=cookies, params=params)
        res.encoding="utf-8"
        items=re.findall("var fc40 = (.*)",res.text)[0]
        new_items=json.loads(items)
        for item in new_items:
            date=item["date"]
            date=datetime.strptime(date,"%Y%m%d").strftime("%Y-%m-%d")
            good_thing=item["alins"]
            bad_thing=item["als"]
            max_weather=item["hmax"]
            min_weather=item["hmin"]
            rain_rate=item["hgl"]
            nl=item["nlyf"]+item["nl"]
            if "2024" in date or date in date_str or "2026" in date:
                continue
            content.append({
                "日期":date,
                "宜":good_thing,
                "不宜":bad_thing,
                "最高温":max_weather,
                "最低温":min_weather,
                "下雨概率":rain_rate,
                "农历":nl
            })
            date_str.append(date)
    if not os.path.exists(f"{province}主要城市天气"):
        os.makedirs(f"{province}主要城市天气")
    path=f"{province}主要城市天气\{city_key}.csv"
    pd.DataFrame(content).to_csv(path,index=False,encoding="utf-8-sig")
    print(f"{city_key}ok")
    time.sleep(1)

if __name__=="__main__":
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.weather.com.cn/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\""
    }
    cookies = {
        "f_city": "%E5%AE%89%E5%BA%86%7C101220601%7C",
        "Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b": "1767172569,1767756298,1769565938",
        "HMACCOUNT": "7AAC1E46B87593CB",
        "Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b": "1769566484"
    }
    params = {
        "_": "1769566570465"
    }
    url = "https://j.i8tq.com/weather2020/search/city.js"
    res1 = requests.get(url, headers=headers)
    n = re.findall("var city_data = (.*)", res1.text, re.S)[0]
    places = json.loads(n)
    province = input("请输入你要查找的省份：")
    city_key=places[province].keys()
    city_value=places[province].values()
    with ThreadPoolExecutor(max_workers=5)as executor:
        executor.map(get_html,city_key,city_value)


