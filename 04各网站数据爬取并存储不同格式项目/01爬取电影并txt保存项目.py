import requests
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor

def get_html(div):
    title=div.xpath('./div/div/div[2]/a/h2/text()')[0]
    type=div.xpath('./div/div/div[2]/div[1]/button[2]/span/text()')[0]
    place=div.xpath('./div/div/div[2]/div[2]/span[1]/text()')[0]
    time=div.xpath('./div/div/div[2]/div[2]/span[3]/text()')[0]
    try:
        date=div.xpath('./div/div/div[2]/div[3]/span/text()')[0]
    except:
        date="无明确上映日期"
    score=div.xpath('./div/div/div[3]/p[1]/text()')[0].strip().replace(" ",'')
    if not os.path.exists("简洁电影网"):
        os.makedirs("简洁电影网")
    path="简洁电影网/电影.txt"
    with open(path,"a",encoding="utf-8") as f:
        f.write(f"电影名称：{title}\n")
        f.write(f"电影类型：{type}\n")
        f.write(f"播出地点：{place}\n")
        f.write(f"时长：{time}\n")
        f.write(f"上映时间：{date}\n")
        f.write(f"电影评分：{score}\n")
        f.write(f"{'='*50}\n")
    print(f"{title}保存完毕")
    time.sleep(1)

if __name__=="__main__":
    for page in range(1,5):
        url = f"https://ssr1.scrape.center/page/{page}"
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"}
        res = requests.get(url, headers=headers)
        tree = etree.HTML(res.text)
        divs = tree.xpath('//*[@id="index"]/div[1]/div[1]/div')
        with ThreadPoolExecutor(max_workers=5)as executor:
            executor.map(get_html,divs)
