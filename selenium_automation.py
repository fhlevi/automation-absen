from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://aos.metranet.co.id/'

browser.get(link)

nik = os.getenv('NIK')
password = os.getenv('PASS')

# login
browser.find_element(By.ID, 'txtusername').send_keys(nik)
browser.find_element(By.ID, 'txtpassword').send_keys(password)
time.sleep(2)
browser.find_element(By.ID, 'btnsubmit').click()
time.sleep(2)

# checkin
browser.find_element(By.ID, 'txtnik').send_keys(nik)
browser.find_element(By.XPATH, '//*[@id="txtworkloc"]/option[3]').click()
browser.find_element(By.XPATH, '//*[@id="txtworkstatus"]/option[2]').click()
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="btnsubmit"]').click()
time.sleep(2)

# checkout
# browser.find_element(By.ID, 'txtnik').send_keys(nik)
# time.sleep(2)
# browser.find_element(By.ID, 'btnsubmit').click()
# time.sleep(3)

