from template.request_generator.base_request import BaseRequest
from template.request_generator.request_type import RequestType


class MakeRecipeRequest(BaseRequest):
    def __init__(self):
        self.__protocolNumber = RequestType.MAKE_RECIPE.value

    def __str__(self):
        return f"GeneratedRecipeRequest(protocolNumber={self.__protocolNumber}"
