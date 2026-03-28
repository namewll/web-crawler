# 目标网址: http://renshi.people.com.cn/
import os.path
import time

from bs4 import BeautifulSoup
import requests

"""
    用Beautifulsoup 解析人民网  提取数据

    用的解释器是哪个？  html.parser    Beautifulsoup自带的解析器  解析速度比较慢  不需要安装

    lxml 解析速度比较快 底层是c语言实现 比html.parser 快5-10倍

    lxml 既可以是解析器 也可以是一个独立的解析库

    安装：pip install lxml -i https://mirrors.aliyun.com/pypi/simple/
"""

url = 'http://renshi.people.com.cn/index1.html'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}

res = requests.get(url,headers=headers)

res.encoding = 'utf-8'

soup = BeautifulSoup(res.text,'lxml')

# 找到所有的新闻
li_tags = soup.find('div',class_='fl').find_all('li')

for li in li_tags:
    # 提取 新闻的标题
    title = li.a.text
    # 提取 新闻的链接
    href = li.a['href']
    # 提取 日期
    date = li.i.text

    # http://renshi.people.com.cn/n1/2025/1217/c139617-40626126.html
    #                            /n1/2025/1217/c139617-40626126.html
    if 'http' not in href:
        href = 'http://renshi.people.com.cn' + href

    # print(href)

    # # 请求详细页面地址
    res_detail = requests.get(href,headers=headers)

    res_detail.encoding = 'utf-8'

    soup_detail = BeautifulSoup(res_detail.text,'lxml')
    # 新闻的详细信息
    p_text = soup_detail.find('div',class_='show_text').text

    # time.sleep(1)

    # 保存到 txt文件
    if not os.path.exists('人民网人事新闻之bs4解析'):
        os.mkdir('人民网人事新闻之bs4解析')

    # 拼接完整路径
    save_path = os.path.join('人民网人事新闻之bs4解析',f'{title}.txt')

    # 搭建一个字符串  先来建立一个列表 存储所有的信息 再转化为字符串
    content = []
    content.append(f'新闻标题:{title}')
    content.append(f'新闻链接:{href}')
    content.append(f'新闻发布日期:{date}')
    content.append('='*50)
    content.append(f'新闻内容:{p_text}')

    # join 就是将列表 拼接为字符串
    text = '\n'.join(content)

    # 写入文本
    # a  追加写入
    # w  覆盖写入

    # 写入二进制
    # ab  追加写入二进制
    # wb  覆盖写入二进制

    with open(save_path,'w',encoding='utf-8') as f:
        f.write(text)

    print(f'保存成功,文件路径是{save_path}')

    time.sleep(1)