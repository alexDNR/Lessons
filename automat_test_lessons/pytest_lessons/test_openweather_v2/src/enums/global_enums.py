from enum import Enum

class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Expected value not received"
    WRONG_DICT_TYPE = "Received value is not a dict"

