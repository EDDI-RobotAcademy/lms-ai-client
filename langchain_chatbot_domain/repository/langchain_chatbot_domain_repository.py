from abc import ABC, abstractmethod

class LangchainChatbotDomainRepository(ABC):
    @abstractmethod
    def loadDocumentation(self, filepath):
        pass

    @abstractmethod
    def generatePrompt(self):
        pass

    @abstractmethod
    def loadEmbeddingModel(self):
        pass

    @abstractmethod
    def createFaissIndex(self, texts, embedding):
        pass

    @abstractmethod
    def loadFaissIndex(self, faissIndexPath, embeddings):
        pass

    @abstractmethod
    def loadLLMChain(self):
        pass

    @abstractmethod
    def createChain(self, llm, prompt, faissIndex):
        pass

    @abstractmethod
    def invokeChain(self, chain, userSendMessage):
        pass
