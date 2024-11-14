import requests


def get(URL):
    res = requests.get(URL)
    return res.status_code


print(get('https://yandex.ru'))
