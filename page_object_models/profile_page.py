from selenium.webdriver.common.by import By

from helpers.table_helper import TableHelper
from helpers.common_actions import CommonActions
from page_object_models.locators.common_components.account_detail_locators import AccountDetailLocators
from page_object_models.locators.common_components.search_box_locators import SearchBoxLocators
from page_object_models.locators.profile_page_locators import ProfilePageLocators


class ProfilePage:
    def __init__(self, sb):
        self.__sb = sb

    def go_to(self):
        self.__sb.open("https://demoqa.com/profile")

        return self

    def search_for_book(self, book_name):
        self.__sb.type(SearchBoxLocators.SEARCH_BOX, book_name)
        self.__sb.click(SearchBoxLocators.SEARCH_BUTTON)

        return self

    def get_books_by_title(self, title):
        return self.__sb.driver.find_elements(by=By.XPATH, value=ProfilePageLocators.BOOK_TITLE.format(title))

    def click_log_out(self):
        self.__sb.click(AccountDetailLocators.LOG_OUT_BUTTON)

        return self

    def click_go_to_book_store(self):
        self.__sb.click(ProfilePageLocators.GO_TO_BOOK_STORE_BUTTON)

        return self

    def click_delete_account(self):
        self.__sb.click(ProfilePageLocators.DELETE_ACCOUNT_BUTTON)

        return self

    def click_confirm_delete_account(self):
        CommonActions(self.__sb).click_confirm_dialog()

        return self

    def click_delete_single_book(self, book_title: str):
        table_helper = TableHelper(self.__sb).wait_for_react_table_exist()
        row_index = table_helper.get_row_index(book_title, 'Title')

        self.__sb.click(ProfilePageLocators.DELETE_BOOK_BUTTON.format(row_index))

        return self

    def click_confirm_delete_book(self):
        CommonActions(self.__sb).click_confirm_dialog()

        return self

    def click_delete_all_books(self):
        self.__sb.click(ProfilePageLocators.DELETE_ALL_BOOKS_BUTTON)

        return self

    def click_confirm_delete_all_books(self):
        CommonActions(self.__sb).click_confirm_dialog()

        return self
