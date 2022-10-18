from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginFormElements:
    driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe')

    USERNAME = driver.find_element(By.XPATH, "//*[@id=\"password\"]")


class LoginForm:
    elements = LoginFormElements()

    def __init__(self):
        super().__init__(By.ID, "user-name")

    def fill_username(self, value: str):
        self.elements.USERNAME.send_keys(value)
