BASE_URL = 'https://demoqa.com'


class Endpoints:
    class Account:
        POST_CHECK_USER_AUTHORIZED = BASE_URL + '/Account/v1/Authorized'
        POST_GENERATE_TOKEN = BASE_URL + '/Account/v1/GenerateToken'
        POST_CREATE_USER = BASE_URL + '/Account/v1/User'
        DELETE_USER = BASE_URL + '/Account/v1/User/{0}'
        GET_USER = BASE_URL + '/Account/v1/User/{0}'

    class BookStore:
        GET_BOOKS = BASE_URL + '/BookStore/v1/Books'
        POST_BOOKS = BASE_URL + '/BookStore/v1/Books'
        DELETE_BOOKS = BASE_URL + '/BookStore/v1/Books'
        GET_BOOK = BASE_URL + '/BookStore/v1/Book'
        DELETE_BOOK = BASE_URL + '/BookStore/v1/Book'
        PUT_BOOK = BASE_URL + '/BookStore/v1/Books/{0}'
