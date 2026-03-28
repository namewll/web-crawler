import requests
import pandas as pd

headers = {
    "accept": "application/graphql+json, application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.imdb.com",
    "priority": "u=1, i",
    "referer": "https://www.imdb.com/",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Google Chrome\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36",
    "x-amzn-sessionid": "141-5507502-8390932",
    "x-imdb-client-name": "imdb-web-next",
    "x-imdb-client-rid": "2VBNAGXCEE19VCY3PHFY",
    "x-imdb-consent-info": "eyJhZ2VTaWduYWwiOiJBRFVMVCIsImlzR2RwciI6ZmFsc2V9",
    "x-imdb-user-country": "CN",
    "x-imdb-user-language": "zh-CN",
    "x-imdb-weblab-treatment-overrides": "{\"IMDB_DISCO_KNOWNFOR_V2_1328450\":\"T1\"}"
}
cookies = {
    "session-id": "141-5507502-8390932",
    "ad-oo": "0",
    "ubid-main": "135-2079154-5346060",
    "ci": "eyJhZ2VTaWduYWwiOiJBRFVMVCIsImlzR2RwciI6ZmFsc2V9",
    "x-main": "siQeSN7zksFzZ@F8t21mhPKEoiqdpGrURAaz?zxcBuIDKPmCh6azOwEsp@W@8pF2",
    "at-main": "Atza|gQANe7mVAwEBAFtWldSmbI3SYqXLACHSI5ffinSQ-Vzd1B_E_gXNqoIWZZJlOhnTXIMZyJishfeBEmY1zTxtwdNFbmp8JfQCbh_7jsXFopC2OSntEqqu3-eQKY5r0ol_CJytvBzTqK7hR4L40CZ7qPToL_lfK1VhLTg2v4w83JhWLgc_RqFK6Mw0QzzQuHSH2xRlv_zdT0Qbwi2scOs4XvenF1RtMWG_y2XNCOvGGQHcgeNtvqKX7wCEeah-o4ivVJLS62tNFuA1v_IJQMEB0qT-u_KZgW6ga6PbWMZv3SaKVICIcdYp4F43dPxHClTTFwDLOjMeUkWD49SNqzUSKYIRrQjzAtB9opVTNvk",
    "sess-at-main": "01/m6XkrDyDuEIbJ/cenHcZRbFaBOG7sQ8CaqGZKDV4=",
    "session-id-time": "2082787201l",
    "log-main": "b9b8bbc3-e494-4eba-8572-75f8b8a7e981",
    "session-token": "UkDanuJs+bxtv6DByoMTyhq0UL0lDpZnZiKgpm/54M0tdsARrboJPSnWz7cgqZ/W/5Eh9WDVaTePI0y0shSfj95w7UtTA4XwlOu0hkAeL26fqEcnHidfPh5Mzlw8davDtsgxvVb2Bqbv0tMws4DMZkeegplaDFHYvpck+eEmBnRO0GaAeIe1RxjCRzId5nPv7vi00sA+rG/zRAS6bvi8YtVTTG2Hv0QgkwIRwx4mVTP9S1247wI+xfwAul6H242Q"
}
params = {
    "operationName": "TitleReviewsRefine",
    "variables": "{\"after\":\"g4xojermtizcs3yc66txtnburhs4ycjs3aodb7xqcwb32u3bnmskudcyoarta4mpvme2oxczrxbjlwrzl2ypw6y\",\"const\":\"tt34956443\",\"filter\":{},\"first\":25,\"isInProfileImageWeblab\":false,\"locale\":\"zh-CN\",\"sort\":{\"by\":\"HELPFULNESS_SCORE\",\"order\":\"DESC\"}}",
    "extensions": "{\"persistedQuery\":{\"sha256Hash\":\"fb58a77d474033025bf28e1fe68f9b998111d3df58e08cd8405bd9265b1a9aff\",\"version\":1}}"
}
content=[]
for page in range(1,50):
    print(f"================={page}==================")
    url = "https://caching.graphql.imdb.com/"
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    data=response.json()["data"]["title"]["reviews"]["pageInfo"]["endCursor"]
    items=response.json()["data"]["title"]["reviews"]["edges"]
    for item in items:
        star_count=item["node"]["authorRating"]
        title=item["node"]["summary"]["originalText"]
        text=item["node"]["text"]["originalText"]["plaidHtml"]
        upVotes=item["node"]["helpfulness"]["upVotes"]
        downVotes=item["node"]["helpfulness"]["downVotes"]
        author=item["node"]["author"]["username"]["text"]
        content.append({
            "星级":star_count,
            "标题":title,
            "内容":text,
            "点赞":upVotes,
            "反对":downVotes,
            "作者":author
        })
        print(author)
pd.DataFrame(content).to_excel("imdb.xlsx", index=False)
print("ok")