from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

###test-1.1.1
def test_edit_first_name():
    my_account_btn = my.driver.find_element(By.CSS_SELECTOR, "sm:flex border border-white rounded-full hidden text-primaryLight hover:text-primaryPurple font-bold px-8 py-2")
    my_account_btn.click()
    personal_details = my.driver.find_element(By.CSS_SELECTOR, "ant-tabs-tab-btn")
    personal_details.click()
    edit_profile = my.driver.find_element(By.CSS_SELECTOR, "font-bold text-primaryPurple px-4 py-2 underline underline-offset-2")
    edit_profile.click()
    first_name = my.driver.find_element(By.CSS_SELECTOR, "ant-input css-3mqfnx border border-primaryDark focus:outline-none focus:border-primaryPurple p-1 rounded-full")
    first_name.click()
    first_name_inner = first_name.get_attribute('innerText')
    assert first_name_inner == 'נועה'
    save_btn = my.driver.find_element(By.CSS_SELECTOR, "ant-btn css-3mqfnx ant-btn-primary w-[130px] text-sm bg-primaryPurple text-white font-bold pb-4 rounded-full my-2 hover:bg-primaryPurple")
    save_btn.click()

