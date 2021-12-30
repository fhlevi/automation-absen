from selenium.webdriver.common.by import By
import time
import config.config_browser as config_browser
import config.config_env as config_env

def login_access():
    config_browser.browser.find_element(By.ID, 'txtusername').send_keys(config_env.nik)
    time.sleep(3)

    config_browser.browser.find_element(By.ID, 'txtpassword').send_keys(config_env.password)
    time.sleep(3)

    config_browser.browser.find_element(By.ID, 'btnsubmit').click()
    time.sleep(2)

def checkin():
    config_browser.browser.find_element(By.ID, 'txtnik').send_keys(config_env.nik)
    time.sleep(3)

    config_browser.browser.find_element(By.XPATH, '//*[@id="txtworkloc"]/option[3]').click()
    time.sleep(3)

    config_browser.browser.find_element(By.XPATH, '//*[@id="txtworkstatus"]/option[2]').click()
    time.sleep(3)

    config_browser.browser.find_element(By.XPATH, '//*[@id="btnsubmit"]').click()
    time.sleep(2)

def checkout():
    config_browser.browser.find_element(By.ID, 'txtnik').send_keys(config_env.nik)
    time.sleep(3)
    
    config_browser.browser.find_element(By.ID, 'btnsubmit').click()
    time.sleep(2)