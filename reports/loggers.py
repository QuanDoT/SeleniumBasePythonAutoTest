def __log__(text):
    print(f'\n{text}')


def info(text):
    __log__(f'--- INFO: {text}')


def warn(text):
    __log__(f'--- WARN: {text}')


def fatal(text):
    raise Exception(f'--- FATAL: {text}')
