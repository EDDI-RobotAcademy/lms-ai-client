from openai_chatbot_domain.repository.openai_chatbot_domain_repository_impl import OpenaiChatbotDomainRepositoryImpl
from openai_chatbot_domain.service.openai_chatbot_service import OpenaiChatbotDomainService


class OpenaiChatbotDomainServiceImpl(OpenaiChatbotDomainService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__openaiChatbotDomainRepository = OpenaiChatbotDomainRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def generateRecipe(self, userSendMessage):
        print(f"starting generate recipe...\ncalling repository->generateRecipe... with {userSendMessage}")
        generatedRecipe = self.__openaiChatbotDomainRepository.generateRecipe(userSendMessage)
        print(f"generatedRecipe: {generatedRecipe}")
        print(f"recipe generating complete... Inserting queue")
        return await generatedRecipe
