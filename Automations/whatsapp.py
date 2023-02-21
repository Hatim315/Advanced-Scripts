from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time     
import undetected_chromedriver as uc
option=uc.ChromeOptions()
option.add_argument("--ignore-certificate-error")
option.add_argument("--ignore-ssl-errors")
option.add_argument("--user-data-dir=jas")
driver=uc.Chrome(options=option)
driver.get("https://web.whatsapp.com/t")
time.sleep(30)
driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div/div[2]').click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p").send_keys("testing...")
time.sleep(3)
driver.find_element(By.CLASS_NAME,'epia9gcq').click()

time.sleep(5000)