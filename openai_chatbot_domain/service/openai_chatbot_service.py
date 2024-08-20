from abc import ABC, abstractmethod


class OpenaiChatbotService(ABC):
    @abstractmethod
    def makeRecipe(self, userSendMessage):
        pass