import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
user_data_dir=r"D:\桌面\爬虫实例\07自动化selenium爬取\user_data_dir"
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.51job.com/")
driver.maximize_window()
seacher=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,".el-input__inner"))
)
seacher.send_keys("Python",Keys.ENTER)
content=[]
for i in range(10):
    items=WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,".joblist-item"))
    )
    for item in items:
        job_name=item.find_element(By.CSS_SELECTOR,".jname.text-cut").text
        company=item.find_element(By.CSS_SELECTOR,".cname.text-cut").text
        salary=item.find_element(By.CSS_SELECTOR,".sal.shrink-0").text
        content.append({
            "职位名称":job_name,
            "公司名称":company,
            "薪资":salary
        })
    driver.find_element(By.CSS_SELECTOR,".btn-next").click()

pd.DataFrame(content).to_csv("Python职位招聘信息.csv",index=False,encoding="utf-8-sig")
print("ok")
time.sleep(1)
