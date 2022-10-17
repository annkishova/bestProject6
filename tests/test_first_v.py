from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def first_test():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver.get("https://www.saucedemo.com/")
    input_username = driver.find_element(By.ID, "user-name")
    if input_username is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")


if __name__ == '__main__':
    first_test()


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


if __name__ == '__main__':
    second_test()
