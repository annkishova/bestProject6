import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def start_browser():
    with ("Запуск браузера"):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

    yield driver

    with ("Закрытие браузера"):
        driver.quit()


@pytest.fixture(scope="function")
def navigate_start_page(start_browser):
    driver = start_browser
    with ("Переход на стартовую страницу"):
        driver.get("https://www.saucedemo.com/")
    
    yield
