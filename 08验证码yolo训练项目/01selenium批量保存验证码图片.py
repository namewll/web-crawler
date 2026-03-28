import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

if not os.path.exists("验证码图片"):
    os.makedirs("验证码图片")

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://captcha1.scrape.center/")
driver.maximize_window()
time.sleep(2)
login=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/button'))
)
login.click()
for i in range(1,64):
    try:
        time.sleep(1)
        canvas=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]'))
        )
        canvas.screenshot(f"验证码图片/img{i}.png")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[6]/div/div[2]/div/a[2]").click()
    except:
        driver.find_element(By.CSS_SELECTOR,".geetest_panel_error_content").click()
print("ok")