from uuid import uuid4

import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Forms.login_form import LoginForm


class TestAuthorization:
    def test_authorization(self, navigate_start_page):
        #"Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)

        #"Заполнить параметр Логин"
        name_login = "standard_user"
        pass_login = "secret_sauce"
        login_form.fill_login_form(name_login, pass_login)
        login_form.click_enter()
