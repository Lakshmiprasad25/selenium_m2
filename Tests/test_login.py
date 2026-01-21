import time
from Pages.LoginPage import LoginPage
from Utilities.excel_reader import read_login_data

def test_orangehrm_login(setup):
    driver=setup
    L=LoginPage(driver)
    data_path=r'C:\Users\Faculty\PycharmProjects\HYBRID\Test_data\login_data.xlsx'
    login_data=read_login_data(data_path)
    for un, pwd in login_data:
        L.login(un,pwd)
        time.sleep(2)
        if "dashboard" not in driver.current_url:
            driver.get_screenshot_as_file(r'C:\Users\Faculty\PycharmProjects\HYBRID\screenshots\failure.png')
            print("Login Failed")
        else:
            print("Login Passed")
            driver.find_element("xpath",'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span').click()
            driver.find_element('xpath','//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a').click()
        time.sleep(2)