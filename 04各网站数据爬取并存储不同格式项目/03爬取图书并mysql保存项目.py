# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='root'
# )
# cursor = conn.cursor()
# sql = """
#     create database if not exists spider default character set utf8mb4;
# """
# cursor.execute(sql)
# conn.commit()
#
# cursor.close()
# conn.close()
#
# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='root',
#     database='spider'
# )
# cursor = conn.cursor()
# sql = """
#     create table if not exists book(
#         id int primary key not null auto_increment comment "序号",
#         title varchar(255) not null comment "书名",
#         price varchar(255) not null comment "价钱",
#         date_ varchar(255) not null comment "时间",
#         publish varchar(255) not null comment "出版社",
#         author varchar(255) not null comment "作者"
#     )
# """
# try:
#     cursor.execute(sql)
#     conn.commit()
# except:
#     conn.rollback()
# cursor.close()
# conn.close()

import pymysql
import requests
from bs4 import BeautifulSoup
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='spider'
)
cursor = conn.cursor()
sql = """
          insert into book values(%s,%s,%s,%s,%s,%s)
      """
for i in range(0,3):
    index=0
    url=f"https://book.douban.com/top250?start={index}"
    index+=25
    headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"}
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,"lxml")
    div=soup.find("div",class_="indent")
    trs=div.find_all("tr",class_="item")
    content=[]
    for tr in trs:
        title=tr.find("div",class_="pl2").a.text.strip().replace("\n","").replace(" ","")
        totals=tr.find("p",class_="pl").text
        sp=totals.split("/ ")
        price=sp[-1]
        date=sp[-2]
        public=sp[-3]
        author=sp[:-3][0]
        try:
            cursor.execute(sql,(0,title,price,date,public,author))
            conn.commit()
        except:
            conn.rollback()
cursor.close()
conn.close()
