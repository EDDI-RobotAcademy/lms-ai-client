from abc import ABC, abstractmethod


class LangchainChatbotDomainService(ABC):
    @abstractmethod
    def getFaissIndex(self):
        pass

    @abstractmethod
    def getGeneratedRecipe(self, userSendMessage):
        pass
