from user_defined_protocol.protocol import UserDefinedProtocolNumber


class ChatLogDomainGetAllResponse:
    def __init__(self, responseData):
        self.protocolNumber = UserDefinedProtocolNumber.GET_ALL_LOGS.value

        for key, value in responseData.items():
            setattr(self, key, value)

    @classmethod
    def fromResponse(cls, responseData):
        return cls(responseData)

    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"ChatLogDomainGetAllResponse({self.__dict__})"