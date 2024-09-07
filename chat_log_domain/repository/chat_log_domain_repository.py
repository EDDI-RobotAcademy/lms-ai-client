from abc import ABC, abstractmethod


class ChatLogDomainRepository(ABC):
    @abstractmethod
    def saveLog(self, account_id, recipe_hash, recipe):
        pass

    @abstractmethod
    def getAllLogs(self):
        pass