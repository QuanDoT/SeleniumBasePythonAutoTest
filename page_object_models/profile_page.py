import allure
from selenium.webdriver.common.by import By

from page_object_models.common_components.confirmation_dialog import ConfirmationDialog
from page_object_models.common_components.react_table import ReactTable
from page_object_models.locators.common_components.account_detail_locators import AccountDetailLocators
from page_object_models.locators.common_components.search_box_locators import SearchBoxLocators
from page_object_models.locators.profile_page_locators import ProfilePageLocators


class ProfilePage:
    def __init__(self, sb):
        self.__sb = sb

    @allure.step('Go to Profile page')
    def go_to(self):
        self.__sb.open("https://demoqa.com/profile")

        return self

    @allure.step('Search for book using book name')
    def search_for_book(self, book_name):
        self.__sb.type(SearchBoxLocators.SEARCH_BOX, book_name)
        self.__sb.click(SearchBoxLocators.SEARCH_BUTTON)

        return self

    def get_books_by_title(self, title):
        return self.__sb.driver.find_elements(by=By.XPATH, value=ProfilePageLocators.BOOK_TITLE.format(title))

    @allure.step('Click Log Out')
    def click_log_out(self):
        self.__sb.click(AccountDetailLocators.LOG_OUT_BUTTON)

        return self

    @allure.step('Click Go to Book Store')
    def click_go_to_book_store(self):
        self.__sb.click(ProfilePageLocators.GO_TO_BOOK_STORE_BUTTON)

        return self

    @allure.step('Click Delete Account')
    def click_delete_account(self):
        self.__sb.click(ProfilePageLocators.DELETE_ACCOUNT_BUTTON)

        return self

    @allure.step('Click Confirm when deleting account')
    def click_confirm_delete_account(self):
        ConfirmationDialog(self.__sb).click_confirm()

        return self

    @allure.step('Delete a single book by clicking the trash icon')
    def click_delete_single_book(self, book_title: str):
        react_table = ReactTable(self.__sb).wait_for_react_table_exist()
        row_index = react_table.get_row_index(book_title, 'Title')

        self.__sb.click(ProfilePageLocators.DELETE_BOOK_BUTTON.format(row_index))

        return self

    @allure.step('Click Confirm when deleting a book in Profile')
    def click_confirm_delete_book(self):
        ConfirmationDialog(self.__sb).click_confirm()

        return self

    @allure.step('Click Delete All Books')
    def click_delete_all_books(self):
        self.__sb.click(ProfilePageLocators.DELETE_ALL_BOOKS_BUTTON)

        return self

    @allure.step('Click Confirm when deleting all books in Profile')
    def click_confirm_delete_all_books(self):
        ConfirmationDialog(self.__sb).click_confirm()

        return self
