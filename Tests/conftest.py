import pytest

@pytest.fixture
def setup():
    import time
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(r'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.close()