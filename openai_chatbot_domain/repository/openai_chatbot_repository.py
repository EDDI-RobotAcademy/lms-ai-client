from abc import ABC, abstractmethod


class OpenaiChatbotRepository(ABC):
    @abstractmethod
    def generateRecipe(self, userSendMessage):
        pass
