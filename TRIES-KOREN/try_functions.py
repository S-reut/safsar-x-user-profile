# driver_set().get
from Project_Data.function_open_driver import driver_set
import time
def test_login():
    base_url = "https://portal-dev.safsarglobal.link/"
    my_driver = driver_set()
    my_driver.get(base_url)
    time.sleep(3)
    login_btn = my_driver.find_element(By.CSS_SELECTOR, "sm:flex hidden text-primaryLight hover:text-primaryPurple font-bold px-8 py-2" or By.href, "/signin")
    login_btn.click()
    time.sleep(3)
