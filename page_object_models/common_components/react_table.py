from helpers.web_element_helper import get_text_from_elements
from page_object_models.locators.common_components.react_table_locators import ReactTableLocators


class ReactTable:
    def __init__(self, sb):
        self.__sb = sb

    def wait_for_react_table_exist(self):
        self.__sb.wait_for_element_visible(ReactTableLocators.TABLE)

        return self

    def get_column_index(self, value_to_match):
        header_elements = self.__sb.find_elements(ReactTableLocators.TABLE_HEADER_CELLS)

        headers = get_text_from_elements(header_elements)

        try:
            index = list(headers).index(value_to_match)
        except ValueError:
            raise Exception(f'Could not find header: "{value_to_match}" in table headers: {headers}')

        return index + 1

    def get_row_index(self, value_to_match, column_to_match: str | int):
        index = None

        if type(column_to_match) is int:
            index = column_to_match
        elif type(column_to_match) is str:
            index = self.get_column_index(column_to_match)

        row_header_elements = self.get_all_elements_in_column(index, locator="//descendant-or-self::*[text()]")

        row_headers = get_text_from_elements(row_header_elements)

        try:
            index = list(row_headers).index(value_to_match)
        except ValueError:
            raise Exception(f'Could not find header: {value_to_match} from table headers: {row_headers}')

        return index + 1

    def get_all_elements_in_column(self, column_index, locator=None):
        elements = self.__sb.find_elements(ReactTableLocators.TABLE_DATA_CELLS_IN_COLUMN.format(column_index) + locator)

        return elements

    def get_all_elements_in_row(self, row_index, locator=None):
        elements = self.__sb.find_elements(ReactTableLocators.TABLE_DATA_CELLS_IN_ROW.format(row_index) + locator)

        return elements
