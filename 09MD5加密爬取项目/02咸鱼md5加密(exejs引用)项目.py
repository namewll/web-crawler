import time
import requests
import hashlib
import execjs

for page in range(1,5):
    headers = {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.goofish.com",
        "priority": "u=1, i",
        "referer": "https://www.goofish.com/",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36"
    }
    cookies = {
        "t": "c4cc6d8948f6cc0f1b512fd02caa1f6a",
        "cna": "sb0JIiEeMkoCAXjyuPlaxKtq",
        "xlly_s": "1",
        "sgcookie": "E100JKr0y9wPYSsqd2atekIto5Swj7oWG7FWEbbsYAWun9LfxtHvKHUenjxNkxBbEGv%2BuUq8fl%2FMA%2BBcaod2xtSFXKJvWQI2OZpeV5%2BFIRFO5TU%3D",
        "tracknick": "xy240190621087",
        "unb": "2221728731250",
        "cookie2": "1dc39a04cc60a7bf80da4f17cb8c554f",
        "mtop_partitioned_detect": "1",
        "_m_h5_tk": "0df3e329dd9e099323b8d7a3234358b4_1770306754667",
        "_m_h5_tk_enc": "49bc09237dac4ae7655fc0e7bdac2bfb",
        "_samesite_flag_": "true",
        "_tb_token_": "580e530346b0e",
        "tfstk": "gSc-H7YoTnxkujOXX_vD-jI04NYDoK0rE0u1tkqldmnx5VSudbVov9no8D2B47cKD2i9zyxrtakqjV1oZLPh97PUOhxMsC0ozWPCxbQ8JaPbryBBtyw7h7zhQ20RXC0rzZ_RAFDXsBUeCoa7ADw7hsazcz67FDwfGyrfNy17RiTY8oNCOuw5GoazS9sSAWTxlozaOziQFE3b0yNQAAedek77v6HxAOahniJf61hYy8EdtoCLGj1gdlZ8mMdtezIaf4ZAO6Z6zOvZk4xR_qVrscUiqI1-X2gZd-hdchEEMqGSdqSJArkIqSZu1L_YZbuSCJG6Y9iTwDesN-QBJ4072SUj1eXamjEoAbeXS1e3Gf2_Nxv2qJV8WDGr2wCIfq0ia-lpXiZEEPPbJX81pkeC4Hhi6VGdjlUhFELAL9y7uolPm0tt8vh_klYX-9WUUOzYjELAL9y7urEMleXFL8WN."
    }
    url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/"
    params = {
        "jsv": "2.7.2",
        "appKey": "34839810",
        "t": f"{int(time.time()*1000)}",
        "sign": "1be4d862c3c8bd1ad869ed49efa2c718",
        "v": "1.0",
        "type": "originaljson",
        "accountSite": "xianyu",
        "dataType": "json",
        "timeout": "20000",
        "api": "mtop.taobao.idlemtopsearch.pc.search",
        "sessionOption": "AutoLoginOnly",
        "spm_cnt": "a21ybx.search.0.0",
        "spm_pre": "a21ybx.home.searchHistory.1.4c053da6KyIzC8",
        "log_id": "4c053da6KyIzC8"
    }
    data = {
        "data": "{\"pageNumber\":"+str(page)+",\"keyword\":\"穿戴甲\",\"fromFilter\":false,\"rowsPerPage\":30,\"sortValue\":\"\",\"sortField\":\"\",\"customDistance\":\"\",\"gps\":\"\",\"propValueStr\":{},\"customGps\":\"\",\"searchReqFromPage\":\"pcSearch\",\"extraFilterValue\":\"{}\",\"userPositionJson\":\"{}\"}"
    }
    content="0df3e329dd9e099323b8d7a3234358b4&"+str(int(time.time()*1000))+"&"+f"{params['appKey']}&"+data["data"]
    with open("11咸鱼md5加密(引用).js", "r", encoding="utf-8")as f:
        data_code=f.read()
    execjs_code=execjs.compile(data_code)
    sign_text=execjs_code.call("i",content)
    params["sign"]=sign_text
    # 1872b03d0dd54201748115ecd9b808b3&1770191992686&34839810&{"pageNumber":1,"keyword":"热水袋","fromFilter":false,"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":{},"customGps":"","searchReqFromPage":"pcSearch","extraFilterValue":"{}","userPositionJson":"{}"}

    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    print(response.text)
    print("="*100)
    time.sleep(1)
