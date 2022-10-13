import pytest
import requests
import json
from resources.data_json_on_python import URL_ENDPOINT, NAME_ADMIN, PASSWORD_ADMIN
import pathlib
from pathlib import Path

path = Path(pathlib.Path.cwd(), "new_user_page.json")


@pytest.fixture
def test_find_page_users():
    response = requests.get(url=URL_ENDPOINT)
    posts = response.json()
    page_users = posts["users"]
    return page_users


def tests_go_page_users_and_login(test_find_page_users):
    url = test_find_page_users


@pytest.fixture
def test_go_page_users_create_json_all_users(test_find_page_users):
    url = test_find_page_users
    result = []
    response_new = requests.get(url, auth=(NAME_ADMIN, PASSWORD_ADMIN)).json()
    temp_result = response_new['results']
    result += temp_result
    while True:
        next_url = response_new['next']
        if not next_url:
            break
        response_new = requests.get(next_url, auth=(NAME_ADMIN, PASSWORD_ADMIN)).json()
        result += response_new['results']

    with open('response.json', 'w') as r:
        json.dump(result, r)


@pytest.fixture
def test_find_new_user_url():
    with open(path, 'r') as file:
        data = json.load(file)
        return data['url']
