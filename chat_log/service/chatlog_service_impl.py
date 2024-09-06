# service/chatlog_service_impl.py
from chat_log.service.chatlog_service import ChatlogService
from chat_log.repository.chatlog_repository import ChatlogRepository
from chat_log.service.request.chatlog_request import ChatlogRequest
from chat_log.service.response.chatlog_response import ChatlogResponse

class ChatlogServiceImpl(ChatlogService):
    def __init__(self, repository: ChatlogRepository):
        self.repository = repository

    def save_log(self, request: ChatlogRequest):
        log_data = request.to_dict()
        log_id = self.repository.save_log(log_data)
        response_data = {"log_id": log_id}
        return ChatlogResponse.from_response(response_data)

    def get_log(self, account_id: str, recipe_hash: str):
        log_data = self.repository.get_log_by_account_and_hash(account_id, recipe_hash)
        if not log_data:
            raise ValueError("Log not found")
        return ChatlogResponse.from_response(log_data)

    def delete_log(self, account_id: str, recipe_hash: str):
        deleted_count = self.repository.delete_log_by_account_and_hash(account_id, recipe_hash)
        return deleted_count > 0

    def get_all_logs(self):
        logs = self.repository.get_all_logs()
        return [ChatlogResponse.from_response(log) for log in logs]
