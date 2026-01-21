class LoginPage:
    username="username"
    password="password"
    login_btn="//button[@type='submit']"

    def __init__(self, driver):
        self.driver=driver

    def login(self, user, pwd):
        self.driver.find_element('name',self.username).clear()
        self.driver.find_element('name',self.username).send_keys(user)
        self.driver.find_element('name',self.password).clear()
        self.driver.find_element('name',self.password).send_keys(pwd)
        self.driver.find_element('xpath',self.login_btn).click()
