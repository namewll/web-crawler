import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"}

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
user_data_dir=r"D:\桌面\爬虫实例\07自动化selenium爬取\user_data_dir"
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.pearvideo.com/popular")
driver.maximize_window()
time.sleep(1)
for i in range(1,9):
    js_code=f"window.scroll(0,{3000*i})"
    driver.execute_script(js_code)
    time.sleep(0.5)
items=WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,".popularem.clearfix"))
)
if not os.path.exists("梨视频"):
    os.makedirs("梨视频")
titles=[]
urls=[]
for item in items:
    title=item.find_element(By.CSS_SELECTOR,".popularem-title").text.replace("?"," ")
    titles.append(title)
    url=item.find_element(By.CSS_SELECTOR,".actplay").get_attribute("href")
    urls.append(url)

for title,url in zip(titles,urls):
    try:
        driver.get(url)
        video=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/video"))
        )
        video_url=video.get_attribute("src")
        print(video_url)
        res=requests.get(video_url,headers=headers)
    except:
        continue
    try:
        path=f"梨视频/{title}.mp4"
        with open(path,"wb")as f:
            f.write(res.content)
    except:
        path="梨视频/wwwwwwwwwwwwwwwww.mp4"
        with open(path,"wb")as f:
            f.write(res.content)
print("ok")



