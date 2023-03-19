import pytest
import requests
from settings2 import valid_email, valid_password


@pytest.fixture(scope='session')
def get_api_key(email: str = valid_email, password: str = valid_password):

    base_url = 'https://petfriends.skillfactory.ru'
    headers = {
        'email': email,
        'password': password
    }

    response = requests.get(base_url + '/api/key', headers=headers)
    status = response.status_code
    try:
        result = response.json()
    except BaseException:
        result = response.text

    return status, result
