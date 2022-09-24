from enum import Enum


class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    USER_NOT_CREATE = 'User not found in file'
    USER_NOT_DELETE = 'User not delete'
    USER_NOT_CHANGE = 'Data users not change'
