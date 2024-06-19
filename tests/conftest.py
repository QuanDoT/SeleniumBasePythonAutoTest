import time
from pathlib import Path
from uuid import uuid4

import allure
import pytest

from constants.dictionaries.books_by_isbn_dictionary import BooksByIsbnDict
from definitions import ROOT_DIR
from helpers.api_helpers import account_api_helper
from helpers.api_helpers import bookstore_api_helper


@pytest.fixture
@allure.title("New authenticated user account")
def valid_account():
    username = 'user' + str(uuid4())
    password = 'Abc@1234'

    create_user_response = account_api_helper.create_user(username, password)
    account_api_helper.generate_token(username, password)
    account_api_helper.check_user_authorized(username, password)

    user_id = create_user_response.json().get('userID')

    yield user_id, username, password

    account_api_helper.delete_user(user_id, username, password)


@pytest.fixture
@allure.title("Authenticated user account, with all books added to its profile")
def profile_with_all_books(valid_account):
    user_id, username, password = valid_account

    all_books_isbn = []

    for key, value in BooksByIsbnDict.items():
        all_books_isbn.append(value)

    bookstore_api_helper.add_books_to_user(user_id, all_books_isbn, username, password)

    return user_id, username, password


# Attach screenshot to Allure Report on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            screenshot_path = Path(ROOT_DIR, 'latest_logs',
                                   rep.nodeid
                                   .replace('tests/', 'tests.').replace('::', '.').replace('.py', '').replace(' ', '_'),
                                   'screenshot.png')

            allure.attach.file(
                screenshot_path,
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f'Failed to take screenshot: {e}')
