import json
from typing import List

import requests
from requests.auth import HTTPBasicAuth

from constants.endpoints import Endpoints
from decorators.requests_decorators import print_response_detail, expect_status_code


@expect_status_code(200)
@print_response_detail
def get_books():
    return requests.get(Endpoints.BookStore.GET_BOOKS)


@expect_status_code(201)
@print_response_detail
def add_books_to_user(userid: str, list_isbn: List, username: str, password: str):
    collection_of_isbns = []

    for isbn in list_isbn:
        collection_of_isbns.append({
            'isbn': str(isbn)
        })

    data = {
        'userId': userid,
        'collectionOfIsbns': collection_of_isbns
    }

    return requests.post(Endpoints.BookStore.POST_BOOKS, json=data, auth=HTTPBasicAuth(username, password))


@expect_status_code(200, 204)
@print_response_detail
def delete_books_from_user(userid: str, username: str, password: str):
    payload = {'UserId': userid}

    return requests.delete(Endpoints.BookStore.DELETE_BOOKS, params=payload, auth=HTTPBasicAuth(username, password))


@expect_status_code(200)
@print_response_detail
def get_book(isbn: str):
    payload = {'ISBN': isbn}

    return requests.get(Endpoints.BookStore.GET_BOOKS, params=payload)


@expect_status_code(204)
@print_response_detail
def delete_book_from_user(userid: str, isbn: str, username: str, password: str):
    data = {
        'isbn': userid,
        'userId': isbn
    }

    return requests.delete(Endpoints.BookStore.DELETE_BOOK, json=data, auth=HTTPBasicAuth(username, password))


@expect_status_code(200)
@print_response_detail
def add_book_to_user(userid: str, isbn: str, username: str, password: str):
    data = {
        'userId': userid,
        'isbn': isbn
    }

    return requests.put(Endpoints.BookStore.PUT_BOOK.format(isbn), json=data, auth=HTTPBasicAuth(username, password))
