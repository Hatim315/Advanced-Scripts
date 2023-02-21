from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
#---------------------------------------ITS A STARTING SCRIPT IN ANOTHER WAY -----------------------------------------------
'''go=Service("/home/jashandeeps/SideProjects")
go.start()
driver=webdriver.Remote(go.service_url)
driver.get(url)'''

#---------------------------------------Below code is undetectable chromedriver code-----------------------------------------------
username=input("enter username: ")
password=input("enter password: ")
options = uc.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--user-data-dir=jas")
driver = uc.Chrome(options=options)
driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S453646576%3A1667457368263195&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAvQpBUqP57na16kvT5rM_mqUXsNhQlKDG8TNCvgazNBb2u62ToEw0V7xhoIVN69tYLKDIL_')

#below code is if our browser has not logged in  ----------------------------------------------------------------------------------------------------------------------------------
time.sleep(9)
try:
   
   driver.find_element(By.ID,"identifierId").send_keys(username)
   driver.find_element(By.CLASS_NAME,"VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()
   time.sleep(5)

   driver.find_element(By.NAME,'Passwd').send_keys(password)
   driver.find_element(By.CLASS_NAME,"VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()

   time.sleep(5)
except:
   print("Already Logged In")
finally:
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   myelem=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'hist_state')))
   for i in range(3):
      driver.find_element(By.CLASS_NAME,"T-Jo").click()

      elements=WebDriverWait(driver,3).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'asa')))
      elements[2].click()
      time.sleep(10)

      time.sleep(5000)
      driver.quit()