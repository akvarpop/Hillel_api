import requests
import json
from configuration import USER_POPRAVKA, USER_POPRAVKA_CHANGE
from resources.data_json_on_python import URL_ENDPOINT, NAME_ADMIN, PASSWORD_ADMIN
from src.enums.global_enums import GlobalErrorMessage
import pathlib
from pathlib import Path

path = Path(pathlib.Path.cwd(), "response.json")


def check_create_user_by_name(result):
    with open(path, 'r') as file:
        data = json.load(file)
    for item in data:
        value = item.get("username", None)
        if value == result:
            return value


def test_creat_new_user(test_find_page_users):
    url = test_find_page_users
    response = requests.request("POST", url, data=USER_POPRAVKA, auth=(NAME_ADMIN, PASSWORD_ADMIN))
    new_user_info = response.json()
    with open('new_user_page.json', 'w') as r:
        json.dump(new_user_info, r)
    assert new_user_info["username"] == USER_POPRAVKA["username"]


def test_user_created(test_go_page_users_create_json_all_users):
    name_user = check_create_user_by_name(USER_POPRAVKA["username"])
    assert name_user == USER_POPRAVKA["username"], GlobalErrorMessage.USER_NOT_CREATE


def test_change_new_user(test_find_new_user_url):
    url = test_find_new_user_url
    response = requests.request("PATCH", url, data=USER_POPRAVKA_CHANGE, auth=(NAME_ADMIN, PASSWORD_ADMIN))
    change_result = response.json()
    assert change_result["username"] == USER_POPRAVKA_CHANGE["username"], GlobalErrorMessage.USER_NOT_CHANGE


def test_delete_user(test_find_new_user_url):
    url = test_find_new_user_url
    response = requests.request("DELETE", url, data=USER_POPRAVKA_CHANGE, auth=(NAME_ADMIN, PASSWORD_ADMIN))
    assert response.status_code == 204, GlobalErrorMessage.USER_NOT_DELETE


def test_check_delete_user(test_go_page_users_create_json_all_users):
    name_user = check_create_user_by_name(USER_POPRAVKA["username"])
    assert name_user != USER_POPRAVKA["username"], GlobalErrorMessage.USER_NOT_DELETE

print(check_create_user_by_name)
