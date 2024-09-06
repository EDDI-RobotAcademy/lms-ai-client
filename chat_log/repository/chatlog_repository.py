from abc import ABC, abstractmethod

class ChatlogRepository(ABC):
    @abstractmethod
    def save_log(self, log_data: dict):
        pass

    @abstractmethod
    def get_log_by_account_and_hash(self, account_id: str, recipe_hash: str):
        pass

    @abstractmethod
    def delete_log_by_account_and_hash(self, account_id: str, recipe_hash: str):
        pass

    @abstractmethod
    def get_all_logs(self):
        pass
