from openai_chatbot_domain.repository.openai_chatbot_repository_impl import OpenaiChatbotRepositoryImpl
from openai_chatbot_domain.service.openai_chatbot_service import OpenaiChatbotService
from openai_chatbot_domain.service.response.make_recipe_responce import GeneratedRecipeResponse
from template.custom_protocol.entity.custom_protocol import CustomProtocolNumber


class OpenaiChatbotServiceImpl(OpenaiChatbotService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__openaiChatbotRepository = OpenaiChatbotRepositoryImpl.getInstance()

        return cls.__instance

    def makeRecipe(self, userSendMessage):
        recipe = self.__openaiChatbotRepository.generateRecipe(userSendMessage)
        return GeneratedRecipeResponse(CustomProtocolNumber.MAKE_RECIPE, recipe)
