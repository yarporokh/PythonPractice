def create_header(func):
    def wrapper():
        return f"<h1>{func()}</h1>"

    return wrapper


def underline_text(func):
    def wrapper():
        return f"<u>{func()}</u>"

    return wrapper


@create_header
@underline_text
def func():
    return "Underlined header"


print(func())  # Output: <h1><u>Underlined header</u></h1>


def runtime(func):
    import time
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time}")

    return wrapper


@runtime
def get_page():
    import requests
    webpage = requests.get('https://google.com')


get_page()  # Output: Execution time: 0.45677924156188965
