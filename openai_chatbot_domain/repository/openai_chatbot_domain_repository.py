from abc import abstractmethod, ABC

class OpenaiChatbotDomainRepository(ABC):
    @abstractmethod
    def generateRecipe(self, userSendMessage):
        pass