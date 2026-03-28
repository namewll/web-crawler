import requests
import pandas as pd

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "referer": "https://m.douban.com/movie/subject/34780991/comments?sort=new_score&start=25&source=",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Google Chrome\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "bid": "N8ad3mNK32E",
    "ap_v": "0,6.0",
    "__utma": "30149280.1288010243.1769421843.1769421843.1771927764.2",
    "__utmc": "30149280",
    "__utmz": "30149280.1771927764.2.2.utmcsr=sec.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
    "dbcl2": "\"293821450:4gq2WzW4hyw\"",
    "ck": "IHWF",
    "push_noty_num": "0",
    "push_doumail_num": "0",
    "__utmv": "30149280.29382",
    "__utmb": "30149280.10.10.1771927764",
    "frodotk": "\"76ad17c2a550b79564074747eff226bf\"",
    "talionusr": "\"eyJpZCI6ICIyOTM4MjE0NTAiLCAibmFtZSI6ICJXTEwifQ==\"",
    "Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2": "1771928240",
    "HMACCOUNT": "7AAC1E46B87593CB",
    "ll": "\"118194\"",
    "_gid": "GA1.2.877576502.1771928241",
    "_ga_Y4GN1R87RG": "GS2.1.s1771928240$o1$g1$t1771928998$j60$l0$h0",
    "_ga": "GA1.1.1070517954.1771928241",
    "Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2": "1771929080",
    "Hm_ck_1771929079618": "42"
}
url = "https://m.douban.com/rexxar/api/v2/movie/34780991/interests"
index=-25
content=[]
for page in range(1,18):
    print(f"第{page}页")
    params = {
        "count": "20",
        "order_by": "hot",
        "anony": "false",
        "start": "0",
        "ck": "IHWF",
        "for_mobile": "1"
    }
    index+=25
    params["start"]=str(index)
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    date=response.json()
    items=date["interests"]
    for item in items:
        author=item["user"]["name"]
        try:
            star_count=item["rating"]["star_count"]
        except:
            star_count=0
        create_time=item["create_time"]
        ip_location=item["ip_location"]
        vote_count=item["vote_count"]
        comment=item["comment"]
        content.append({
            "作者":author,
            "星级":star_count,
            "时间":create_time,
            "地址":ip_location,
            "有用数量":vote_count,
            "内容":comment
        })
        print(author)
pd.DataFrame(content).to_excel("哪吒之魔童闹海短评.xlsx",index=False)
print("ok")


