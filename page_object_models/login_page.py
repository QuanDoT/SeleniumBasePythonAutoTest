from page_object_models.locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, sb):
        self.__sb = sb

    def go_to(self):
        self.__sb.open("https://demoqa.com/login")

        return self

    def input_username(self, username):
        self.__sb.type(LoginPageLocators.USERNAME_INPUT, username)

        return self

    def input_password(self, password):
        self.__sb.type(LoginPageLocators.PASSWORD_INPUT, password)

        return self

    def click_login(self):
        self.__sb.click(LoginPageLocators.LOGIN_BUTTON)

        return self

    def do_login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

        return self
