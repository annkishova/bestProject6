from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginFormElements:
    USERNAME = (By.XPATH, "//*[@id=\"password\"]")


class LoginForm:
    element = LoginFormElements

    def __init__(self):
        pass

    def fill_username(self, value: str):
        self.element.USERNAME.send_keys(value)
