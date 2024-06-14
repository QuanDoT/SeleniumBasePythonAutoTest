import pytest

from constants.enums.book_titles_enum import BookTitlesEnum
from page_object_models.locators.login_page_locators import LoginPageLocators
from page_object_models.locators.profile_page_locators import ProfilePageLocators
from page_object_models.login_page import LoginPage
from page_object_models.profile_page import ProfilePage


class TestProfile:
    def test_login_with_valid_credential_then_delete_account(self, valid_account, sb):
        user_id, username, password = valid_account

        login_page = LoginPage(sb)
        (login_page
         .go_to()
         .do_login(username, password))

        (ProfilePage(sb)
         .click_delete_account()
         .click_confirm_delete_account())

        login_page.do_login(username, password)

        sb.assert_text('Invalid username or password!', LoginPageLocators.INVALID_CREDENTIAL_TEXT)

    @pytest.mark.parametrize('book_title',
                             [BookTitlesEnum.Git_Pocket_Guide.value,
                              BookTitlesEnum.Learning_JavaScript_Design_Patterns.value])
    def test_login_then_remove_one_added_book(self, book_title: str, profile_with_all_books, sb):
        user_id, username, password = profile_with_all_books

        login_page = LoginPage(sb)
        (login_page
         .go_to()
         .do_login(username, password))

        profile_page = ProfilePage(sb)
        (profile_page
         .click_delete_single_book(book_title)
         .click_confirm_delete_book())

        sb.assert_element_absent(ProfilePageLocators.BOOK_TITLE.format(book_title))

    def test_login_then_remove_existing_books_in_profile(self, profile_with_all_books, sb):
        user_id, username, password = profile_with_all_books

        login_page = LoginPage(sb)
        (login_page
         .go_to()
         .do_login(username, password))

        profile_page = ProfilePage(sb)
        (profile_page
         .click_delete_all_books()
         .click_confirm_delete_all_books())

        for title in BookTitlesEnum:
            sb.assert_element_absent(ProfilePageLocators.BOOK_TITLE.format(title))
