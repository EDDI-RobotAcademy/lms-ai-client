from abc import ABC, abstractmethod
from service.request.chatlog_request import ChatlogRequest
from service.response.chatlog_response import ChatlogResponse

class ChatlogService(ABC):
    @abstractmethod
    def save_log(self, request: ChatlogRequest):
        pass

    @abstractmethod
    def get_log(self, account_id: str, recipe_hash: str):
        pass

    @abstractmethod
    def delete_log(self, account_id: str, recipe_hash: str):
        pass

    @abstractmethod
    def get_all_logs(self):
        pass
