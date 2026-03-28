import time
import requests
import hashlib
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
        "cookie2": "1ee02310f384fe92e0d9e4858a32e958",
        "mtop_partitioned_detect": "1",
        "_m_h5_tk": "1872b03d0dd54201748115ecd9b808b3_1770200525675",
        "_m_h5_tk_enc": "9ad05fe5947c2d3b474f979367c41237",
        "_samesite_flag_": "true",
        "_tb_token_": "58f377f3a6d85",
        "sgcookie": "E100JKr0y9wPYSsqd2atekIto5Swj7oWG7FWEbbsYAWun9LfxtHvKHUenjxNkxBbEGv%2BuUq8fl%2FMA%2BBcaod2xtSFXKJvWQI2OZpeV5%2BFIRFO5TU%3D",
        "tracknick": "xy240190621087",
        "csg": "bde8c641",
        "unb": "2221728731250",
        "tfstk": "gfetnnjg3wbMJsXCydfhmeQyP5s3M6qasPrWnq0MGyULVu8iGRDgkIUg0rcf7A2YJoaRbmbanhPUru9gI1kDHAkqhablETqgbxkjCb_O7FkIc0Rfnc9jQvO7SlBRETqafhm1qk6usjS_EmujhfGXdHgEDKT_lj9QA2oqcFiXCMEI829scm9bAvimVI9blxsLA2ovhxG_lvsK02gjhxM9KC32fqpY9PfpvxdyPKv0pchtkK0pHWeHEjg7B2AlHyn9z4ZsJK9jPGRlakEGWLrnQ84-qPXBBzEb4SGLHe_-uJEQCSZeWZiUGPDISY16vA2af7GbFZRbyAUxNRGpciEgfVHKA8sDa22KSrwtOgv-ivwoNANhTNcmB0UbQPKvhzZ3qRlUHaLIu5mrdmeVVI3xGgRaE8E7HU0-mCsdvIRq1DuUQe41yoPYFD3lvQd2gfAqv4jdvIRq1DoKrMdJgIlMg"
    }
    url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/"
    params = {
        "jsv": "2.7.2",
        "appKey": "34839810",
        "t": f"{int(time.time()*1000)}",
        "sign": "79a4843db714effdd353357113b9c0a7",
        "v": "1.0",
        "type": "originaljson",
        "accountSite": "xianyu",
        "dataType": "json",
        "timeout": "20000",
        "api": "mtop.taobao.idlemtopsearch.pc.search",
        "sessionOption": "AutoLoginOnly",
        "spm_cnt": "a21ybx.search.0.0",
        "spm_pre": "a21ybx.home.searchInput.0"
    }
    data = {
        "data": "{\"pageNumber\":"+str(page)+",\"keyword\":\"热水袋\",\"fromFilter\":false,\"rowsPerPage\":30,\"sortValue\":\"\",\"sortField\":\"\",\"customDistance\":\"\",\"gps\":\"\",\"propValueStr\":{},\"customGps\":\"\",\"searchReqFromPage\":\"pcSearch\",\"extraFilterValue\":\"{}\",\"userPositionJson\":\"{}\"}"
    }

    content="1872b03d0dd54201748115ecd9b808b3&"+str(int(time.time()*1000))+"&"+f"{params['appKey']}&"+data["data"]
    md5_obj = hashlib.md5()
    md5_obj.update(content.encode())
    sign_text=md5_obj.hexdigest()
    params["sign"]=sign_text
    # 1872b03d0dd54201748115ecd9b808b3&1770191992686&34839810&{"pageNumber":1,"keyword":"热水袋","fromFilter":false,"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":{},"customGps":"","searchReqFromPage":"pcSearch","extraFilterValue":"{}","userPositionJson":"{}"}

    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    print(response.text)
    print("="*100)
    time.sleep(1)
