from enum import Enum

class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Expected value not received"
    WRONG_LEN_POSTS = "Expected len response not received"