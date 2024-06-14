from uuid import uuid4

import pytest

from constants.dictionaries.books_by_isbn_dictionary import BooksByIsbnDict
from helpers.api_helpers import account_api_helper
from helpers.api_helpers import bookstore_api_helper


@pytest.fixture
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
def profile_with_all_books(valid_account):
    user_id, username, password = valid_account

    all_books_isbn = []

    for key, value in BooksByIsbnDict.items():
        all_books_isbn.append(value)

    bookstore_api_helper.add_books_to_user(user_id, all_books_isbn, username, password)

    yield user_id, username, password

    bookstore_api_helper.delete_books_from_user(user_id, username, password)
