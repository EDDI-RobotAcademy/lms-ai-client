from abc import ABC, abstractmethod


class ChatLogDomainService(ABC):
    @abstractmethod
    def saveLog(self, account_id, recipe_hash, recipe):
        pass

    @abstractmethod
    def getAllLogs(self):
        pass

    @abstractmethod
    def deleteLog(self, account_id, recipe_hash):
        pass

    def getLog(self, account_id, recipe_hash):
        pass
