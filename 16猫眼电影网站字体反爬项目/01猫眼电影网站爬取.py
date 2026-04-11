import requests
from bs4 import BeautifulSoup
import re
from fontTools.ttLib import TTFont
import xmltodict
import pandas as pd
import time

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Referer": "https://www.maoyan.com/board/6?timeStamp=1775825948997&channelId=40011&index=8&signKey=69b6a8f78fa4be044bc849e9482183a8&sVersion=1&webdriver=false",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"146\", \"Not-A.Brand\";v=\"24\", \"Microsoft Edge\";v=\"146\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "__mta": "152491910.1775825917946.1775825917946.1775825917946.1",
    "uuid_n_v": "v1",
    "uuid": "FADFB39034DC11F1A87D03DC2914E4E87AA2D0B320DD40A79C7A74D1D174ED51",
    "_csrf": "8276367630f4c76bd55ea773ff985a5a51a2e7557773cc6d213d53a0ff2e0e3c",
    "_lxsdk_cuid": "19d777916d7c8-02c01e876d6ae7-4c657b58-168000-19d777916d7c8",
    "_lxsdk": "FADFB39034DC11F1A87D03DC2914E4E87AA2D0B320DD40A79C7A74D1D174ED51",
    "_ga": "GA1.1.995175611.1775825918",
    "Hm_lvt_e0bacf12e04a7bd88ddbd9c74ef2b533": "1775825918",
    "HMACCOUNT": "67A7773FF32FE2A7",
    "global-guide-isclose": "true",
    "_ga_WN80P4PSY7": "GS2.1.s1775825917$o1$g1$t1775825949$j28$l0$h0",
    "Hm_lpvt_e0bacf12e04a7bd88ddbd9c74ef2b533": "1775825949",
    "_lxsdk_s": "19d777916d8-323-3fe-39e%7C%7C12"
}
input_type=input('请输入你想看的电影类型,比如(最受期待榜、国内票房榜、北美票房榜):')
if input_type=='国内票房榜':
    url = f"https://www.maoyan.com/board/1"
elif input_type=='最受期待榜':
    url = f"https://www.maoyan.com/board/6"
elif input_type=='北美票房榜':
    url = f"https://www.maoyan.com/board/2"
content=[]
pages=int(input('请输入你想看的页数：'))
for page in range(1,pages+1):
    params = {
        "timeStamp": f"{int(time.time())}",
        "channelId": "40011",
        "signKey": "bcfa2e1d5bf3b06466e05ef9da916d66",
        "sVersion": "1",
        "webdriver": "false",
        'offset':f'{(page-1)*10}'
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    soup=BeautifulSoup(response.text, 'lxml')
    font_text=soup.find('style').text
    # print(font_text)
    # https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/20a70494.woff
    #       //s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/75e5b39d.woff"
    load_url=re.findall(",url(.*?);}",font_text)[0].replace('("','').replace('")','')
    end_load_href='https:'+load_url
    res=requests.get(end_load_href,headers=headers, cookies=cookies)
    file_name=load_url.split('/')[-1]
    with open(file_name,'wb')as f:
        f.write(res.content)
    font=TTFont(file_name)
    font.saveXML(file_name.split('.')[0]+'.xml')
    with open(f"{file_name.split('.')[0]}.xml",'r',encoding='utf-8')as f:
        file_text=f.read()
    dict_text=xmltodict.parse(file_text)
    TTGlyphs=dict_text['ttFont']['glyf']['TTGlyph']
    one_dict={}
    two_dict={}
    for ttglyph in TTGlyphs[1:-1]:
        two_count=0
        if type(ttglyph['contour'])!=list:
            one_count=len(ttglyph['contour']['pt'])
        else:
            one_count = len(ttglyph['contour'][0]['pt'])
            two_count=len(ttglyph['contour'][1]['pt'])
        two_dict[ttglyph['@name']] = two_count
        one_dict[ttglyph['@name']] = one_count
    data=[]
    for i in one_dict:
        data.append((i, one_dict[i],two_dict[i]))
    data.sort(key=lambda x:(x[1],x[2]),reverse=True)
    unicode_sort=[]
    for i in data:
        j=i[0].replace('uni','&#x').lower()
        unicode_sort.append(j)
    num_sort=[3,2,9,6,5,0,8,7,1,4]
    result=response.text
    for index in range(len(unicode_sort)):
        result=result.replace(unicode_sort[index]+';',str(num_sort[index]))
    soup=BeautifulSoup(result,'html.parser')
    dds=soup.find_all('dd')
    for dd in dds:
        title=dd.a['title']
        print(title)
        img_src=dd.a.find_all('img')[1]['data-src']
        ps=dd.find_all('p')
        try:
            actors=ps[1].text.replace('主演：','')
            update_time=ps[2].text.replace('上映时间：','')
            time_tickets=ps[3].text.replace('\n','').replace(' ','').replace('实时票房:','').replace('本月新增想看：','')
            total_tickets=ps[4].text.replace('\n','').replace(' ','').replace('总票房:','').replace('总想看：','')
        except:
            update_time = ps[1].text.replace('上映时间：', '')
            time_tickets = ps[2].text.replace('\n', '').replace(' ', '').replace('实时票房:', '').replace('本月新增想看：','')
            total_tickets = ps[3].text.replace('\n', '').replace(' ', '').replace('总票房:', '').replace('总想看：','')
        content.append({
            '电影名称':title,
            '背景图片':img_src,
            '主演':actors,
            '上映时间':update_time,
            '实时票房':time_tickets,
            '总票房':total_tickets
        })
pd.DataFrame(content).to_excel('maoyan.xlsx',index=False)
print('ok')


