from _pytest.outcomes import fail

from reports.loggers import info


def print_response_detail(func):
    def decorator(*args, **kwargs):
        response = func(*args, **kwargs)

        info(f'Sent {response.request.method} request to endpoint: {response.request.url}'
             f'\n| Headers: {response.request.headers} '
             f'\n| Body: {response.request.body} '
             f'\n|  and received response with code {response.status_code}: '
             f'\n| Headers: {response.headers} '
             f'\n| Body: {response.text}')

        return response

    return decorator


def expect_status_code(*dargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            list_decorator_args = []

            for darg in dargs:
                list_decorator_args.append(darg)

            if len(list_decorator_args) > 0 and response.status_code not in list_decorator_args:
                assert fail(f'Expected response status code to be: {dargs}, '
                            f'but found: {response.status_code}')

            return response

        return wrapper

    return decorator
