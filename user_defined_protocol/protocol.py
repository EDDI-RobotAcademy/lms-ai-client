from enum import Enum


class UserDefinedProtocolNumber(Enum):
    # 예약된 정보 (1, 2, 11, 12, 13, 21) 을 제외하고 사용하도록 함
    FIRST_USER_DEFINED_FUNCTION_FOR_TEST = 5
    MAKE_RECIPE = 43
    MAKE_AUDIO = 44
    MAKE_RECIPE_WITH_RETRIEVER = 45
    MAKE_DOCS_FAISS_INDEX = 46

    GET_LOG = 55
    GET_ALL_LOGS = 100
    DELETE_LOG = 54
    SAVE_LOG = 56

    @classmethod
    def hasValue(cls, value):
        return any(value == item.value for item in cls)