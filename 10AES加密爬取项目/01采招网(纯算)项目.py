from Crypto.Cipher import AES
import base64
import requests

def decrypt(key,iv,ciphertext):
    de_base64_text=base64.b64decode(ciphertext)
    cipher = AES.new(key,AES.MODE_CBC,iv)
    decrypt_text=cipher.decrypt(de_base64_text).decode()
    return decrypt_text

headers = {
    "accept": "text/plain, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://search.bidcenter.com.cn",
    "priority": "u=1, i",
    "referer": "https://search.bidcenter.com.cn/",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
url = "https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx"
data = {
    "from": "6137",
    "guid": "643a5787-30d4-4c91-a8f7-af4b0d6e3602",
    "location": "6138",
    "token": "",
    "keywords": "%e5%9b%ad%e6%9e%97+%e7%bb%bf%e5%8c%96",
    "mod": "0"
}
key=b"3zKzyf6eEfuDjAG3"
iv=b"fyUANZ0qSNZhhNCV"
response = requests.post(url, headers=headers, data=data)
print(response.text)
result=decrypt(key,iv,response.text)
# print(result[:-7])


