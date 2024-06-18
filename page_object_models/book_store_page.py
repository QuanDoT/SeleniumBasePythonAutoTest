import allure
from selenium.webdriver.common.by import By

from helpers.web_element_helper import get_text_from_elements
from page_object_models.locators.book_store_page_locators import BookStorePageLocators
from page_object_models.locators.common_components.account_detail_locators import AccountDetailLocators
from page_object_models.locators.common_components.search_box_locators import SearchBoxLocators


class BookStorePage:
    def __init__(self, sb):
        self.__sb = sb

    @allure.step('Go to BookStore page')
    def go_to(self):
        self.__sb.open("https://demoqa.com/books")

        return self

    @allure.step('Search for book')
    def search_for_book(self, text):
        self.__sb.type(SearchBoxLocators.SEARCH_BOX, text)
        self.__sb.click(SearchBoxLocators.SEARCH_BUTTON)

        return self

    @allure.step('Click Log Out')
    def click_log_out(self):
        self.__sb.click(AccountDetailLocators.LOG_OUT_BUTTON)

        return self

    def get_book_titles(self):
        book_title_elements = self.__sb.driver.find_elements(by=By.XPATH, value=BookStorePageLocators.BOOK_TITLES)

        return get_text_from_elements(book_title_elements)
