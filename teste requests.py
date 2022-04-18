import requests

def test_valida_1():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    r = requests.get(url)

    assert True if r.status_code == 200 else False, r.status_code


def test_valida_2():
    url = "https://jsonplaceholder.typicode.com/todos/2"

    r = requests.get(url)

    assert True if r.status_code == 200 else False, r.status_code


def test_valida_3():
    url = "https://jsonplaceholder.typicode.com/todos/nada"

    r = requests.get(url)

    assert True if r.status_code == 200 else False, r.status_code
