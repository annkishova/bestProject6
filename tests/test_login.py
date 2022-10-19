from Forms.login_form import LoginForm
from tests.constants import Sign, Url


class TestAuthorization:
    def test_authorization(self, navigate_start_page):
        driver = navigate_start_page
        #"Перейти к форме авторизации"
        login_form = LoginForm(navigate_start_page)

        #"Заполнить параметр Логин"
        login_form.fill_login_form(Sign.name_login, Sign.pass_login)
        login_form.click_enter()
        current_url = driver.current_url
        assert Url.main_page_url == current_url, "основная страница"
