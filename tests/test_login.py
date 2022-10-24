from forms.login_form import LoginForm
from tests.constants import Sign, Url, ERROR
from selenium.webdriver.common.by import By
import random
import string


class TestAuthorization:
    def test_authorization_empty(self, navigate_start_page):
        driver = navigate_start_page
        #"Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)
        #Попытка авторизации с незаполненными полями
        login_form.click_enter()
        current_url = driver.current_url
        assert login_form.check_exists_error(), "Не отображается ошибка авторизации "
        assert Url.login_url == current_url, "Переход на страницу магазина без авторизации"

    def test_authorization_after_clear_value(self, navigate_start_page):
        driver = navigate_start_page
        # "Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)
        #Заполнить логин, пароль
        login_form.fill_login_username(Sign.name_login)
        login_form.fill_login_password(Sign.pass_login)
        # Очистить поля логин, пароль
        login_form.clear_username_login()
        login_form.clear_password_login()
        login_form.click_enter()
        assert login_form.check_exists_error(), "Не отображается ошибка авторизации"
        text = login_form.get_text(ERROR.error_name)
        assert text == "Epic sadface: Username is required"
        current_url = driver.current_url
        assert Url.login_url == current_url, "Переход на страницу магазина без авторизации"

    def test_authorization_check_valid_login(self, navigate_start_page):
        driver = navigate_start_page
        # "Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)
        # Попытка авторизации с валидным логином и пустым паролем
        login_form.fill_login_username(Sign.name_login)
        login_form.click_enter()
        current_url = driver.current_url
        assert login_form.check_exists_error(), "Не отображается ошибка авторизации "
        text = login_form.get_text(ERROR.error_pass)
        assert text == "Epic sadface: Password is required"
        assert Url.login_url == current_url, "Переход на страницу магазина без авторизации"

    def test_authorization_check_valid_password(self, navigate_start_page):
        driver = navigate_start_page
        # "Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)
        # Попытка авторизации с валидным паролем и пустым логином
        login_form.fill_login_password(Sign.pass_login)
        login_form.clear_username_login()
        assert driver.find_element(By.ID, "user-name").text == ""
        login_form.click_enter()
        current_url = driver.current_url
        assert login_form.check_exists_error(), "Не отображается ошибка авторизации "
        text = login_form.get_text(ERROR.error_name)
        assert text == "Epic sadface: Username is required"
        assert Url.login_url == current_url, "Переход на страницу магазина без авторизации"

    def test_authorization_check_invalid_login_password(self, navigate_start_page):
        driver = navigate_start_page
        # "Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)
        # Попытка авторизации с невалидными логином, паролем
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        random_pass = ''.join(random.choices(string.digits, k=5))
        login_form.fill_login_username(random_name)
        login_form.fill_login_password(random_pass)
        login_form.click_enter()
        current_url = driver.current_url
        assert login_form.check_exists_error(), "Не отображается ошибка авторизации "
        text = login_form.get_text(ERROR.invalid_name_pass)
        assert text == "Epic sadface: Username and password do not match any user in this service"
        assert Url.login_url == current_url, "Переход на страницу магазина без авторизации"

    def test_authorization_succesfull_authorization(self, navigate_start_page):
        driver = navigate_start_page
        # "Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)
        #"Заполнить параметр Логин валидными значениями"
        login_form.fill_login_username(Sign.name_login)
        login_form.fill_login_password(Sign.pass_login)
        login_form.click_enter()
        current_url = driver.current_url
        assert Url.main_page_url == current_url, "Основная страница"
