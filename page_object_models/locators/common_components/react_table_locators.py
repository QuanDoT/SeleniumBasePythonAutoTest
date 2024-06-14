class ReactTableLocators:
    TABLE = '.rt-table'
    TABLE_HEADER_CELLS = '.rt-resizable-header-content'
    TABLE_DATA_CELLS = '//*[@class="rt-tr-group"]//*[@class="rt-td"]'
    TABLE_DATA_CELLS_IN_COLUMN = '//*[@class="rt-tr-group"]//*[@class="rt-td"][{0}]'
    TABLE_DATA_CELLS_IN_ROW = '//*[@class="rt-tr-group"][{0}]//*[@class="rt-td"]'

    JUMP_TO_PAGE_INPUT = '//input[@aria-label="jump to page"]'
    TOTAL_PAGES_ELEMENT = '//*[@class="-totalPages"]'
    ROWS_PER_PAGE_SELECT = '//*[@aria-label="rows per page"]'
    PREVIOUS_BUTTON = '//button[text()="Previous"]'
    NEXT_BUTTON = '//button[text()="Next"]'
