import os.path
import time

import pandas as pd
import aiohttp
import asyncio
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\""
}
params = {
    "limit": "18",
    "offset": "0"
}
content=[]
async def first(i):
    async with aiohttp.ClientSession() as session:
        url = "https://spa5.scrape.center/api/book/"
        params["offset"] = f"{(i - 1) * 18}"
        async with session.get(url, headers=headers, params=params)as res:
            data = await res.json()
            tasks=[]
            for book in data["results"]:
                book_id = book["id"]
                url1 = f"https://spa5.scrape.center/api/book/{book_id}/"
                tasks.append(asyncio.create_task(second(session,url1)))
                await asyncio.gather(*tasks)

async def second(session,url1):
    async with session.get(url1,headers=headers)as res1:
        res1.encoding="utf-8"
        get_text = await res1.json()
        try:
            book_name = get_text["name"].strip().replace("\n",'')
            author = ','.join(get_text["authors"]).strip().replace("\n",'')
            price=get_text["price"].strip().replace("\n",'')
            publish_time=get_text["published_at"].strip().replace("\n",'')
            page=get_text["page_number"]
            sum_text=get_text["introduction"].strip().replace("\n",'')
            content.append({
                "书名":book_name,
                "作者":author,
                "定价":price,
                "出版时间":publish_time,
                "页数":page,
                "简介":sum_text
            })
            print(f"{book_name}保存完毕")
        except Exception as e:
            print(f"略过====={e}")

async def main():
    tasks1=[asyncio.create_task(first(i)) for i in range(1,10)]
    await asyncio.gather(*tasks1)

if __name__ == "__main__":
    asyncio.run(main())
    if not os.path.exists("scrape图书"):
        os.makedirs("scrape图书")
    pd.DataFrame(content).to_csv("scrape图书.csv",index=False,encoding="utf-8-sig")
    print("ok")



