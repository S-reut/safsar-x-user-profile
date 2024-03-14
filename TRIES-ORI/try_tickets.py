import time
from function_open_driver import driver_set





def test_web():
    my_driver = driver_set()
    my_driver.get("https://portal-dev.safsarglobal.link/")

    time.sleep(3)