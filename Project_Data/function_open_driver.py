from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def driver_set():
    chrome_options = Options()
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('disable-extensions')
    chrome_service = Service(ChromeDriverManager().install())
    my_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return my_driver

