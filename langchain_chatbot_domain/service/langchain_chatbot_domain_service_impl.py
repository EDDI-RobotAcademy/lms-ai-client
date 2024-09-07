from langchain_chatbot_domain.repository.langchain_chatbot_domain_repository_impl import \
    LangchainChatbotDomainRepositoryImpl
from langchain_chatbot_domain.service.langchain_chatbot_domain_service import LangchainChatbotDomainService


class LangchainChatbotDomainServiceImpl(LangchainChatbotDomainService):
    FILE_PATH = 'assets/rag_data_963.json'
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__langchainRepository = LangchainChatbotDomainRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def getFaissIndex(self):
        documentList = self.__langchainRepository.loadDocumentation(self.FILE_PATH)
        embedding = self.__langchainRepository.loadEmbeddingModel()
        await self.__langchainRepository.createFaissIndex(documentList, embedding)

    async def getGeneratedRecipe(self, userSendMessage):
        embedding = self.__langchainRepository.loadEmbeddingModel()
        faissIndex = self.__langchainRepository.loadFaissIndex(faissIndexPath='assets/faiss_index_file',
                                                               embeddings=embedding)
        llm = self.__langchainRepository.loadLLMChain()
        prompt = self.__langchainRepository.generatePrompt()
        chain = self.__langchainRepository.createChain(llm, prompt, faissIndex)
        response = await self.__langchainRepository.invokeChain(chain, userSendMessage)

        return {'recipe': response}
