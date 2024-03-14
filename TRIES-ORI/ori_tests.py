import time
from Project_Data.function_open_driver import driver_set
from Project_Data.login_func import login_proccess

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





"rc-tabs-0-tab-כרטיסים"

def test_opentickets():
    my_driver = driver_set()
    my_driver.get("https://portal-dev.safsarglobal.link/")
    login_header_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "התחברות")))
    login_header_element.click()
    phone_num_field_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.NAME, "phone")))
    phone_num_field_element.send_keys("0542433208")
    login_btn_element = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'כניסה')]")))
    login_btn_element.click()
    WebDriverWait(my_driver, 30).until(EC.url_to_be("https://portal-dev.safsarglobal.link/"))
    my_account_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/button[1]")))
    my_account_element.click()
    tickets_section_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.ID, "rc-tabs-0-tab-כרטיסים")))
    tickets_section_element.click()
    time.sleep(10)