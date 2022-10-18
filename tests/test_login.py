from uuid import uuid4

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Forms.login_form import LoginForm


class TestAuthorization:
    def test_authorization(self, navigate_start_page):
        #"Перейти к форме авторизации"
        login_form = LoginForm()

        #"Заполнить параметр Логин"
        random_name_login = str(uuid4())
        user_name = login_form.fill_username(random_name_login)
        assert user_name == "", "Имя не заполнено"
