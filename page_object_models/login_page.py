import allure

from page_object_models.locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, sb):
        self.__sb = sb

    @allure.step('Go to Login page')
    def go_to(self):
        self.__sb.open("https://demoqa.com/login")

        return self

    @allure.step('Type username')
    def input_username(self, username):
        self.__sb.type(LoginPageLocators.USERNAME_INPUT, username)

        return self

    @allure.step('Type password')
    def input_password(self, password):
        self.__sb.type(LoginPageLocators.PASSWORD_INPUT, password)

        return self

    @allure.step('Click Login')
    def click_login(self):
        self.__sb.click(LoginPageLocators.LOGIN_BUTTON)

        return self

    def do_login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

        return self
