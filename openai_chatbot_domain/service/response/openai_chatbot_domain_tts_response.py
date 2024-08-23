from user_defined_protocol.protocol import UserDefinedProtocolNumber


class OpenaiChatbotDomainTTSResponse:
    def __init__(self, responseData):
        self.protocolNumber = UserDefinedProtocolNumber.MAKE_AUDIO.value

        for key, value in responseData.items():
            setattr(self, key, value)

    @classmethod
    def fromResponse(cls, responseData):
        return cls(responseData)

    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"OpenaiChatbotDomainTTSResponse({self.__dict__})"