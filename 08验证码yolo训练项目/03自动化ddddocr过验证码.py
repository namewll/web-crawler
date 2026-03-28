from selenium import webdriver
from ddddocr import DdddOcr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://captcha7.scrape.center/")
driver.maximize_window()
user_name=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/form/div[1]/div/div/input"))
)
user_name.send_keys("admin")
password=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/form/div[2]/div/div/input"))
)
password.send_keys("admin")

canvas=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/form/div[3]/div/div/div[2]/div/canvas")
docr=DdddOcr()
text=docr.classification(canvas.screenshot_as_png)
yzm=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/form/div[3]/div/div/div[1]/div/input"))
)
yzm.send_keys(text)
login=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,".el-button.login.el-button--primary"))
)
login.click()
print("ok")
input()
