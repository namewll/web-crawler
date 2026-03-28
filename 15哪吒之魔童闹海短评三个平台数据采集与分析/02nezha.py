import requests
import pandas as pd

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "referer": "https://www.rottentomatoes.com/m/ne_zha_ii/reviews/all-audience",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Google Chrome\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36"
}
cookies = {
    "akamai_generated_location": "{\"zip\":\"\"\"\",\"city\":\"TONGSHAN\",\"state\":\"JS\",\"county\":\"\"\"\",\"areacode\":\"\"\"\",\"lat\":\"32.34\",\"long\":\"119.11\",\"countrycode\":\"CN\"}",
    "akacd_RTReplatform": "2147483647~rv=4~id=41ab21eaf5e9326bc4c6459190840e6e",
    "eXr91Jra": "A1Dzjo-cAQAAa44wHJsyh4EMRcXDmP2q2ohBIX4JhH61jhYlXXo4EHNXOfz-AXjytpGucmVTwH8AAEB3AAAAAA|1|0|b9834b934c394a1d1fb7bedf941783e1565f0d5f",
    "usprivacy": "1---",
    "__host_color_scheme": "xgOZgKQ6-qMw0UcPJk2LLbKNALqCnPWdUKUuQMjzrVoClyGr2N8s",
    "__host_theme_options": "1771935094201",
    "AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg": "1",
    "s_cc": "true",
    "algoliaUT": "4ad802ab-0d65-4476-9517-c358b87e4522",
    "AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg": "-408604571%7CMCIDTS%7C20509%7CMCMID%7C78163054789562488671814394652758990974%7CMCAAMLH-1772539894%7C11%7CMCAAMB-1772539894%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1771942294s%7CNONE%7CMCSYNCSOP%7C411-20516%7CvVersion%7C4.6.0",
    "check": "true",
    "mbox": "session#1ca143de5a124021abed86e1699248b1#1771936957|PC#1ca143de5a124021abed86e1699248b1.38_0#1835179897",
    "__gads": "ID=3c66cfa5ac089064:T=1771935059:RT=1771935059:S=ALNI_MYgmkd5Er2RGtwbxhqASSTudxO2ng",
    "__gpi": "UID=00001209b8a0a37c:T=1771935059:RT=1771935059:S=ALNI_MbIvOX0_6HkRfeMkO8rID-kv9nDGw",
    "__eoi": "ID=c12e4a417925a208:T=1771935059:RT=1771935059:S=AA-AfjbOfY-ufNLjc4vg9FiloRcs",
    "_cb": "0r3lFDKcHQtCDZDOH",
    "_chartbeat2": ".1771935098173.1771935098173.1.nkkSeC3wmZnC0WvpVfqWbhCs0nEB.1",
    "_cb_svref": "external",
    "_ALGOLIA": "anonymous-33b57de3-7ce2-4380-88fd-1c91baaffbf8",
    "OptanonAlertBoxClosed": "2026-02-24T12:11:38.861Z",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Tue+Feb+24+2026+20%3A11%3A38+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202506.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=88d01174-3a4d-407b-b520-7b5a2a6b5ba4&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=4%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1",
    "OneTrustWPCCPAGoogleOptOut": "false",
    "sailthru_pageviews": "3",
    "_awl": "2.1771935062.5-bec4e5321c939d28486a31ef5ac4ae36-6763652d75732d7765737431-0",
    "cto_bundle": "UBKZWl9zeEdXJTJCdWw1NFIlMkJHV09MaVpkZGZFa3R2WFg2OTd5bnJrWVA4YkVsVnBoaFF3RGd2dnJuUmZ4bSUyRkVTNDklMkJxbHhSb2ZxcFU4aWRoWG5MNmg4NSUyRjRrRzZHVHMxYVdhJTJCc1FMJTJGY1p5ZTRZcFlNMHRoNUE4YlZEdVJ0VkZPUno5bktic3BiVCUyQkZjeHU2dDBXOWUyWXVZZ29nJTNEJTNE",
    "QSI_HistorySession": "https%3A%2F%2Fwww.rottentomatoes.com%2Fm%2Fne_zha_ii%2Freviews%2Fall-audience~1771935116073",
    "s_sq": "wbrosrottentomatoes%3D%2526c.%2526a.%2526activitymap.%2526page%253Drt%252520%25257C%252520movies%252520%25257C%252520reviews%2526link%253DLOAD%252520MORE%2526region%253Dmain-page-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c"
}
params = {
    "after": "",
    "before": "",
    "pageCount": "20",
    "topOnly": "false",
    "type": "audience",
    "verified": "false"
}
url = "https://www.rottentomatoes.com/napi/rtcf/v1/movies/032b21a3-f547-44e9-bfc7-7910475d08e5/reviews"
content=[]
for page in range(1,50):
    print(f"====================={page}========================")
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    items=response.json()["reviews"]
    after=response.json()["pageInfo"]["endCursor"]
    params["after"] = after
    for item in items:
        author=item.get("displayName","匿名用户")
        star_count=item["rating"]
        text=item["review"]
        print(author)
        content.append({
            "作者":author,
            "星级":star_count,
            "内容":text
        })
pd.DataFrame(content).to_excel("nezha.xlsx",index=False)
print("ok")

