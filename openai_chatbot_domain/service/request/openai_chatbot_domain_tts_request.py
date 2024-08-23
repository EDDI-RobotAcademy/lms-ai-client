import sys
import os

from template.request_generator.base_request import BaseRequest

sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'template'))

from user_defined_protocol.protocol import UserDefinedProtocolNumber


class OpenaiChatbotDomainTTSRequest(BaseRequest):
    def __init__(self, **kwargs):
        self.__protocolNumber = UserDefinedProtocolNumber.MAKE_RECIPE.value
        self.parameterList = kwargs.get('chatbotMessage', str)
        self.parameterList = kwargs.get('voiceActor', str)

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
        return f"OpenaiChatbotDomainTestRequest(protocolNumber = {self.__protocolNumber}, parameterList = {self.parameterList})"
