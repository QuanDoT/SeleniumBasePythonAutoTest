import pytest

from page_object_models.locators.common_components.account_detail_locators import AccountDetailLocators
from page_object_models.locators.login_page_locators import LoginPageLocators
from page_object_models.login_page import LoginPage


class TestLogin:
    def test_login_with_valid_credential_should_be_successful(self, valid_account, sb):
        user_id, username, password = valid_account

        login_page = LoginPage(sb)
        (login_page
         .go_to()
         .do_login(username, password))

        sb.assert_text(username, AccountDetailLocators.USERNAME_VALUE_ELEMENT)

    @pytest.skip('To be unskipped when demoing report screen capture on failure function')
    def test_login_deliberate_fail(self, valid_account, sb):
        user_id, username, password = valid_account

        login_page = LoginPage(sb)
        (login_page
         .go_to()
         .do_login(username, password))

        sb.assert_text("WRONG_TEXT", AccountDetailLocators.USERNAME_VALUE_ELEMENT)

    @pytest.mark.parametrize('username, password',
                             [('username1', 'password1'),
                              ('username 2', 'password 2'),
                              (' ', ' ')])
    def test_login_with_invalid_credential_should_be_unsuccessful(self, username, password, sb):
        login_page = LoginPage(sb)
        (login_page
         .go_to()
         .do_login(username, password))

        sb.assert_text('Invalid username or password!', LoginPageLocators.INVALID_CREDENTIAL_TEXT)
