from user_defined_protocol.protocol import UserDefinedProtocolNumber

class ChatlogResponse:
    def __init__(self, response_data):
        self.protocolNumber = UserDefinedProtocolNumber.SAVE_CHAT_LOG.value
        for key, value in response_data.items():
            setattr(self, key, value)

    @classmethod
    def from_response(cls, response_data):
        return cls(response_data)

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"ChatlogResponse({self.__dict__})"
