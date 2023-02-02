from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
#below is the code without uc-----------------------------------------------------------------------------------------------------------------------------------------------------------
go=Service("/home/jashandeeps/SideProjects")
go.start()
option=Options()
option.add_argument("--window-size=1920,1080")
driver=webdriver.Remote(go.service_url,options=option)
essay='''It has long been a subject of discussion about whether the older generation prefers to spend their entire lives in  one place or not, the former notion has several strong elements that deserve attention, and I will explain why using pertinent arguments.
There are myriad arguments in favor of my viewpoint, the most notable one, to start with, lies in the fact that they should become more careful with their decisions. For example, in India, a survey conducted by a university team, which reveals that 90 percent of people benefits from this development, whereas only 10 percent of people face obstacles due to it. Therefore, it is clear that why majority of people agree with this notion.
Another argument supporting my side, is that government and academics have become stronger dealing with this situation. As per my academic research, carried out by Canadian Government reveals that 60 percent of citizens benefits from government reforms. Thus, this trend not only make people more careful, but also make people good life stranded.
To conclude it, although there are some drawbacks of this trend, yet I believe that the advantages of this trend are more in number. In my opinion, it is wise to say that the old generation prefer to spend their entire lives in only one place.'''

#-------------------------Below code is for making chromedriver undetectable-------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
options = uc.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

options.add_argument( "--user-data-dir=<Your chrome profile>")

options.add_argument("--window-size=1920,1080") # I can even use driver.maximize_window() if i dont want to use options
driver = uc.Chrome(options=options)'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
driver.get("https://www.languageacademy.com.au/auth/login")
username="jojohaneysing@gmail.com"
password="14424280j"
driver.find_element(By.NAME,"email").send_keys(username)
driver.find_element(By.NAME,"password").send_keys(password)
driver.find_element(By.CLASS_NAME,"themeBtn").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,'caret').click()
time.sleep(5)
lnks=WebDriverWait(driver,3).until(EC.presence_of_all_elements_located((By.TAG_NAME,'a')))# alternative: driver.find_elements(By.TAG_NAME,'a')
lnks[5].click()
time.sleep(3)
w=driver.find_elements(By.CLASS_NAME,'alert-warning')
w[1].click()
time.sleep(3)
m=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/a')
m.click()
time.sleep(3)

driver.find_element(By.ID,'textBox').send_keys(essay)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div[2]/div/div/div[2]/div/div/div[1]/button[1]').click()

time.sleep(500)
driver.quit()