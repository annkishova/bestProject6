from uuid import uuid4

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Forms.login_form import LoginForm


class TestAuthorization:
    def test_authorization(self, start_browser):
        with ("Перейти к форме авторизации"):
            login_form = LoginForm()

        with ("Заполнить параметр Логин"):
            random_name_login = str(uuid4())
            user_name = login_form.fill_username(random_name_login)
            assert user_name == "", "Имя не заполнено"


def second_test():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element(By.XPATH, "//*[@id=\"user-name\"]")
    input_password = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    login_button = driver.find_element(By.XPATH, "//*[@id=\"login-button\"]")

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element(By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
    if title_text.text == "PRODUCTS":
        print("Мы попали на главную страницу")
    else:
        print("Ошибка поиска элемента")

    time.sleep(5)


if __name__ == '__main__':
    second_test()
