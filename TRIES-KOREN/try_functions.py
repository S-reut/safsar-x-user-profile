# driver_set().get
from Project_Data.function_open_driver import driver_set

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# def test_login():
#     base_url = "https://portal-dev.safsarglobal.link/"
#     my_driver = driver_set()
#     my_driver.get(base_url)
#     time.sleep(3)
#     login_btn = my_driver.find_element(By.CSS_SELECTOR, "sm:flex hidden text-primaryLight hover:text-primaryPurple font-bold px-8 py-2" or By.href, "/signin")
#     login_btn.click()
#     time.sleep(3)


def test_login_proccess_edit_first_name():
    my_driver = driver_set()
    my_driver.get("https://portal-dev.safsarglobal.link/")
    login_header_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "התחברות")))
    time.sleep(2)
    login_header_element.click()
    phone_num_field_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.NAME, "phone")))
    phone_num_field_element.send_keys('0502587365')
    time.sleep(1)
    login_btn_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'כניסה')]")))
    login_btn_element.click()
    WebDriverWait(my_driver, 30).until(EC.url_to_be("https://portal-dev.safsarglobal.link/"))
    time.sleep(5)
    my_account_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/nav/div[1]/ul/button')))
    my_account_btn.click()
    time.sleep(2)
    # personal_details_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ant-tabs-tab-btn")))
    # personal_details_btn.click()
    edit_profile_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.ID, "rc-tabs-0-panel-tab1" and By.CSS_SELECTOR,'#rc-tabs-0-panel-tab1 > div > div:nth-child(1) > button')))
    edit_profile_btn.click()
    time.sleep(5)
    first_name_field_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "//input[@id='firstName']")))
    first_name_field_element.clear()
    first_name_field_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
    first_name_field_element.send_keys("נועה")
    time.sleep(3)
    save_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
    save_btn.click()
    time.sleep(3)
    my_driver.quit()
    my_driver.close()


def test_login_proccess_edit_last_name():
    my_driver = driver_set()
    # action = ActionChains(my_driver)
    my_driver.get("https://portal-dev.safsarglobal.link/")
    login_header_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "התחברות")))
    time.sleep(2)
    login_header_element.click()
    phone_num_field_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.NAME, "phone")))
    phone_num_field_element.send_keys('0544803749')
    time.sleep(1)
    login_btn_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'כניסה')]")))
    login_btn_element.click()
    WebDriverWait(my_driver, 30).until(EC.url_to_be("https://portal-dev.safsarglobal.link/"))
    time.sleep(5)
    my_account_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/nav/div[1]/ul/button')))
    my_account_btn.click()
    time.sleep(2)
    # personal_details_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ant-tabs-tab-btn")))
    # personal_details_btn.click()
    edit_profile_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body/div[@id="root"]/main[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]')))
    edit_profile_btn.click()
    last_name_field_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "//input[@id='lastName']")))
    last_name_field_element.clear()
    time.sleep(3)
    last_name_field_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
    last_name_field_element.send_keys("לוי")
    time.sleep(5)
    save_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
    save_btn.click()
    time.sleep(3)


###0502587365