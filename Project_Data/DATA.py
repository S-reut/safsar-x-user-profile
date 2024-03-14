from function_open_driver import driver_set
base_url = "https://portal-dev.safsarglobal.link/"
login_btn_xpath = "//button[contains(text(),'כניסה')]"
###test-1.1.1
#####edit_first_name:
    first_name_1 = 'נועה'
    my_account_btn = my_driver.find_element(By.CSS_SELECTOR, "sm:flex border border-white rounded-full hidden text-primaryLight hover:text-primaryPurple font-bold px-8 py-2")
    personal_details = my_driver.find_element(By.CSS_SELECTOR, "ant-tabs-tab-btn")
    edit_profile = my_driver.find_element(By.CSS_SELECTOR, "font-bold text-primaryPurple px-4 py-2 underline underline-offset-2")
    first_name = my_driver.find_element(By.CSS_SELECTOR, "ant-input css-3mqfnx border border-primaryDark focus:outline-none focus:border-primaryPurple p-1 rounded-full")
    save_btn = my_driver.find_element(By.CSS_SELECTOR, "ant-btn css-3mqfnx ant-btn-primary w-[130px] text-sm bg-primaryPurple text-white font-bold pb-4 rounded-full my-2 hover:bg-primaryPurple")


###test-1.1.2
####edit_last_name:
    my_account_btn =  my_driver.find_element(By.CSS_SELECTOR, "sm:flex border border-white rounded-full hidden text-primaryLight hover:text-primaryPurple font-bold px-8 py-2")
    personal_details =  my_driver.find_element(By.CSS_SELECTOR, "ant-tabs-tab-btn")
    edit_profile =  my_driver.find_element(By.CSS_SELECTOR, "font-bold text-primaryPurple px-4 py-2 underline underline-offset-2")
    last_name =  my_driver.find_element(By.CSS_SELECTOR, "ant-input css-3mqfnx border border-primaryDark focus:outline-none focus:border-primaryPurple p-1 rounded-full mr-4")
    last_name_inner = last_name.get_attribute('innerText')
    save_btn =  my_driver.find_element(By.CSS_SELECTOR, "ant-btn css-3mqfnx ant-btn-primary w-[130px] text-sm bg-primaryPurple text-white font-bold pb-4 rounded-full my-2 hover:bg-primaryPurple")


###test-1.1.3
##edit_email_113:
    my_account_btn =  my_driver.find_element(By.CSS_SELECTOR, "sm:flex border border-white rounded-full hidden text-primaryLight hover:text-primaryPurple font-bold px-8 py-2")
    personal_details =  my_driver.find_element(By.CSS_SELECTOR, "ant-tabs-tab-btn")
    edit_profile =  my_driver.find_element(By.CSS_SELECTOR, "font-bold text-primaryPurple px-4 py-2 underline underline-offset-2")
    email_field = my_driver.find_element(By.CSS_SELECTOR, "ant-input css-3mqfnx w-full border border-primaryDark focus:outline-none focus:border-primaryPurple p-1 rounded-full"
                                         or By.ID, "email")
    save_btn =  my_driver.find_element(By.CSS_SELECTOR, "ant-btn css-3mqfnx ant-btn-primary w-[130px] text-sm bg-primaryPurple text-white font-bold pb-4 rounded-full my-2 hover:bg-primaryPurple")



###test-1.1.14
##click_edit_tab:
    my_account_btn =  my_driver.find_element(By.CSS_SELECTOR, "sm:flex border border-white rounded-full hidden text-primaryLight hover:text-primaryPurple font-bold px-8 py-2")    personal_details = my.driver.find_element(By.CSS_SELECTOR, "ant-tabs-tab-btn")
    edit_profile =  my_driver.find_element(By.CSS_SELECTOR, "font-bold text-primaryPurple px-4 py-2 underline underline-offset-2")



###test-
###click edit phone
edit_phone_btn =  my_driver.find_element(By.CSS_SELECTOR, "font-bold text-primaryPurple px-4 py-2 underline underline-offset-2")
user_phone_filed =  my_driver.find_element(By.ID,"phone")
save_phone_btn =  my_driver.find_element(By.CSS_SELECTOR, "w-[130px] bg-primaryPurple text-white font-bold p-2 rounded-full font-bold text-systemLight px-4 py-2 mt-2")
