class Url:
    login_url = "https://www.saucedemo.com/"
    main_page_url = "https://www.saucedemo.com/inventory.html"


class Sign:
    name_login = "standard_user"
    pass_login = "secret_sauce"


class ERROR:
    error_pass = "//h3[contains(text(), 'Password is required')]"
    error_name = "//h3[contains(text(), 'Username is required')]"
    invalid_name_pass = "//h3[contains(text(), 'Username and password do not match')]"
