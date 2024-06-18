from helpers.web_element_helper import get_text_from_elements
from page_object_models.locators.common_components.html_table_locators import HtmlTableLocators


class HtmlTable:
    def __init__(self, sb):
        self.__sb = sb

    def wait_for_table_exist(self):
        self.__sb.wait_for_element_visible(HtmlTableLocators.TABLE)

        return self

    def get_table_body_texts_as_dict(self):
        table_headers = self.get_table_headers()

        if len(table_headers) != 2:
            raise Exception('Only tables with 2 columns are supported!')

        table_body_rows = self.get_table_body_rows()

        table_body_as_dict = dict()
        for i in range(1, len(table_body_rows) + 1):
            row_data = get_text_from_elements(self.__sb.find_elements(HtmlTableLocators.TABLE_DATA_CELLS.format(i)))

            row_data_as_list = list(row_data)

            table_body_as_dict.update({row_data_as_list[0]: row_data_as_list[1]})

        return table_body_as_dict

    def get_table_headers(self):
        return self.__sb.find_elements(HtmlTableLocators.TABLE_HEADERS)

    def get_table_body_rows(self):
        return self.__sb.find_elements(HtmlTableLocators.TABLE_BODY_ROWS)
