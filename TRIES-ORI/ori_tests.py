import time
from Project_Data.function_open_driver import driver_set
from Project_Data.login_func import login_proccess

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

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

def test_tickets_sold_2_2_1():
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
    my_account_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/button[1]")))
    my_account_element.click()
    tickets_section_element = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.ID, "rc-tabs-0-tab-כרטיסים")))
    tickets_section_element.click()
    ticket_sold = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]")))
    assert ticket_sold.is_displayed()
    time.sleep(5)


def test_tickets_sold_2_2_2():
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
    my_account_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/button[1]")))
    my_account_element.click()
    tickets_section_element = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.ID, "rc-tabs-0-tab-כרטיסים")))
    tickets_section_element.click()
    time.sleep(5)
    delete_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[7]/img[1]")))
    delete_btn.click()
    time.sleep(5)
    confirm_delete_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'מחיקה')]")))
    confirm_delete_btn.click()
    time.sleep(2)
    tickets_section_element = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.ID, "rc-tabs-0-tab-כרטיסים")))
    tickets_section_element.click()
    time.sleep(5)
    assert delete_btn == NoSuchElementException

def test_division_2_3_1():
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
    division_line = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#rc-tabs-0-panel-כרטיסים > div > hr:nth-child(3)")))
    assert division_line.is_displayed()
    time.sleep(4)