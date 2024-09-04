import sys
import os

from template.request_generator.base_request import BaseRequest

sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'template'))

from user_defined_protocol.protocol import UserDefinedProtocolNumber


class LangchainChatbotDomainRequest(BaseRequest):
    def __init__(self, **kwargs):
        self.__protocolNumber = UserDefinedProtocolNumber.MAKE_RECIPE_WITH_RETRIEVER.value
        self.parameterList = kwargs.get('data', [])

    def getProtocolNumber(self):
        return self.__protocolNumber

    def getParameterList(self):
        return tuple(self.parameterList)

    def toDictionary(self):
        return {
            "protocolNumber": self.__protocolNumber,
            "parameterList": self.parameterList
        }

    def __str__(self):
        return f"LangchainChatbotDomainRequest(protocolNumber = {self.__protocolNumber}, parameterList = {self.parameterList})"
