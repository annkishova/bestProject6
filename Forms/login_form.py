from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginFormElements:
    USERNAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.ID, "login-button")


class LoginForm(BasePage):
    element = LoginFormElements

    def fill_login_form(self, username: str, password: str):
        self.driver.find_element(*self.element.USERNAME).send_keys(username)
        self.driver.find_element(*self.element.PASSWORD).send_keys(password)

    def click_enter(self):
        self.driver.find_element(*self.element.LOGIN_BUTTON).click()
