import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from ultralytics import YOLO
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://captcha1.scrape.center/")
driver.maximize_window()
user_name=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/form/div[1]/div/div/input"))
)
user_name.send_keys("admin")
password=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/form/div[2]/div/div/input"))
)
password.send_keys("admin")
time.sleep(2)
login=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/form/div[3]/div/button"))
)
login.click()
time.sleep(2)
canvas=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".geetest_canvas_bg.geetest_absolute"))
)
canvas.screenshot("img1.png")
model=YOLO("best.pt")
result=model("img1.png",conf=0.5)
x1,y1,x2,y2=result[0].boxes.xyxy.cpu().numpy()[0]
move_duration=x1
time.sleep(1)
action=ActionChains(driver)
button=driver.find_element(By.CSS_SELECTOR, ".geetest_slider_button")
action.click_and_hold(button).perform()
action.move_by_offset(xoffset=move_duration+3,yoffset=0).perform()
time.sleep(1)
action.release().perform()
time.sleep(3)





