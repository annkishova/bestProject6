from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginFormElements:
    USERNAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_LABEL = (By.CLASS_NAME, "error-message-container")

    # IS_VISIBLE = expected_conditions.visibility_of_element_located


class LoginForm(BasePage):
    element = LoginFormElements

    # @property
    # def is_error_authorization(self) -> bool:
    #     res = self.element.ERROR_LABEL

    def check_exists_error(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "error-message-container")
        except NoSuchElementException:
            return False
        return True

    def fill_login_username(self, username: str):
        self.driver.find_element(*self.element.USERNAME).send_keys(username)

    def fill_login_password(self, password: str):
        self.driver.find_element(*self.element.PASSWORD).send_keys(password)

    def click_enter(self):
        self.driver.find_element(*self.element.LOGIN_BUTTON).click()

    def clear_username_login(self):
        self.driver.find_element(*self.element.USERNAME).clear()

    def clear_password_login(self):
        self.driver.find_element(*self.element.PASSWORD).clear()

    def get_text(self, elem_name):
        res = self.driver.find_element(By.XPATH, f"{elem_name}")
        return res.text
