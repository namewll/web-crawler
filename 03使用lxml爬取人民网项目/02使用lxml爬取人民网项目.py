# 目标网址: http://renshi.people.com.cn/
import os
import time

from lxml import etree
import requests
from concurrent.futures import ThreadPoolExecutor

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}
# 对于每一个li标签的解析
def precess_news(news):
    # 获取新闻标题
    title = news.xpath('./a/text()')[0]
    # print(title)
    # 获取新闻链接
    href = news.xpath('./a/@href')[0]

    if 'http' not in href:
        href = 'http://renshi.people.com.cn' + href

    # 获取新闻的发布时间
    date = news.xpath('./i/text()')[0]

    # print(date)

    # # 请求详细页面地址
    res_detail = requests.get(href,headers=headers)

    res_detail.encoding = 'utf-8'

    etree_detail = etree.HTML(res_detail.text)

    # /html/body/div[7]/div[1]/div/div[3]/p

    text_detail = etree_detail.xpath('/html/body/div[7]/div[1]/div/div[3]/p')

    content = []

    content.append(f'新闻标题:{title}')
    content.append(f'新闻链接:{href}')
    content.append(f'新闻发布日期:{date}')
    content.append('=' * 50)
    for text in text_detail:
        if text.xpath("./text()"):
            content.append(f'新闻内容:{text.xpath("./text()")[0]}')

    # join 就是将列表 拼接为字符串
    text = '\n'.join(content)

    # 保存到 txt文件
    if not os.path.exists('人民网人事新闻之lxml解析'):
        os.mkdir('人民网人事新闻之lxml解析')

    # 拼接完整路径
    save_path = os.path.join('人民网人事新闻之lxml解析', f'{title}.txt')

    with open(save_path,'w',encoding='utf-8') as f:
        f.write(text)

    print(f'保存成功,文件路径是{save_path}')

    time.sleep(1)


if __name__ == '__main__':
    for i in range(1,8):
        url = f'http://renshi.people.com.cn/index{i}.html'

        res = requests.get(url, headers=headers)

        res.encoding = 'utf-8'

        tree = etree.HTML(res.text)

        # /html/body/div[6]/div[1]/ul/li
        news_items = tree.xpath('/html/body/div[6]/div[1]/ul/li')

        # 启动线程池
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(precess_news,news_items)

        print(f'第{i}页处理完成！！！！！！！')
        time.sleep(1)

    print('所有文本处理完毕!!!!!')



# 打包工具 安装pip install pyinstaller

# 打开终端 输入命令：pyinstaller -F 路径(指向py文件)

# 创建虚拟环境打包 ： 只把需要的库 安装 然后打包
#



