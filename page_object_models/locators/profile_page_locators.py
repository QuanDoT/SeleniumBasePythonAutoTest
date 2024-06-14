class ProfilePageLocators:
    GO_TO_BOOK_STORE_BUTTON = '#gotoStore'
    DELETE_ACCOUNT_BUTTON = '//button[text()="Delete Account"]'
    DELETE_ALL_BOOKS_BUTTON = '//div[@class="text-right button di"]//child::button[text()="Delete All Books"]'
    BOOK_TITLES = 'xpath=//span[@class="mr-2"]//a'
    BOOK_TITLE = '//div[@class="ReactTable -striped -highlight"]//child::a[text()={0}]'
    DELETE_BOOK_BUTTON = '(//*[@class="action-buttons"]//*[@id="delete-record-undefined"])[{0}]'
    DELETE_BOOK_BUTTONS = '//*[@class="action-buttons"]//*[@id="delete-record-undefined"]'
