from requests.auth import HTTPBasicAuth

from constants.endpoints import Endpoints
from decorators.requests_decorators import print_response_detail, expect_status_code
from helpers.api_helpers.request_helper import get_session


@expect_status_code(200)
@print_response_detail
def check_user_authorized(username: str, password: str):
    data = {
        'userName': username,
        'password': password
    }

    return get_session().post(Endpoints.Account.POST_CHECK_USER_AUTHORIZED, json=data)


@expect_status_code(200)
@print_response_detail
def generate_token(username: str, password: str):
    data = {
        'userName': username,
        'password': password
    }

    return get_session().post(Endpoints.Account.POST_GENERATE_TOKEN, json=data)


@expect_status_code(201)
@print_response_detail
def create_user(username: str, password: str):
    data = {
        'userName': username,
        'password': password
    }

    return get_session().post(Endpoints.Account.POST_CREATE_USER, json=data)


@expect_status_code(204, 200)
@print_response_detail
def delete_user(userid: str, username: str, password: str):
    return get_session().delete(Endpoints.Account.DELETE_USER.format(userid), auth=HTTPBasicAuth(username, password))


@expect_status_code(200)
@print_response_detail
def get_user(userid: str, username: str, password: str):
    return get_session().get(Endpoints.Account.GET_USER.format(userid), auth=HTTPBasicAuth(username, password))
