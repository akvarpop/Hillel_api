from tests.test_aqa import check_create_user_by_name
from configuration import USER_POPRAVKA, USER_POPRAVKA_CHANGE
name_user = check_create_user_by_name(["username"])

print(name_user)