import os
import sys

from chat_log_domain.service.chat_log_domain_service_impl import ChatLogDomainServiceImpl
from chat_log_domain.service.request.chat_log_domain_delete_request import ChatLogDomainDeleteRequest
from chat_log_domain.service.request.chat_log_domain_get_all_request import ChatLogDomainGetAllRequest
from chat_log_domain.service.request.chat_log_domain_get_request import ChatLogDomainGetRequest
from chat_log_domain.service.request.chat_log_domain_save_request import ChatLogDomainSaveRequest
from chat_log_domain.service.response.chat_log_domain_delete_response import ChatLogDomainDeleteResponse
from chat_log_domain.service.response.chat_log_domain_get_all_response import ChatLogDomainGetAllResponse
from chat_log_domain.service.response.chat_log_domain_get_response import ChatLogDomainGetResponse
from chat_log_domain.service.response.chat_log_domain_save_response import ChatLogDomainSaveResponse
from first_user_defined_function_domain.service.fudf_service_impl import FudfServiceImpl
from first_user_defined_function_domain.service.request.fudf_just_for_test_request import FudfJustForTestRequest
from first_user_defined_function_domain.service.response.fudf_just_for_test_response import FudfJustForTestResponse
from langchain_chatbot_domain.service.langchain_chatbot_domain_service_impl import LangchainChatbotDomainServiceImpl
from langchain_chatbot_domain.service.request.langchain_chatbot_domain_get_faiss_request import \
    LangchainChatbotDomainGetFaissRequest
from langchain_chatbot_domain.service.request.langchain_chatbot_domain_request import LangchainChatbotDomainRequest
from langchain_chatbot_domain.service.response.langchain_chatbot_domain_get_faiss_response import \
    LangchainChatbotDomainGetFaissResponse
from langchain_chatbot_domain.service.response.langchain_chatbot_domain_response import LangchainChatbotDomainResponse
from openai_chatbot_domain.service.openai_chatbot_service_impl import OpenaiChatbotDomainServiceImpl
from openai_chatbot_domain.service.request.openai_chatbot_domain_request import OpenaiChatbotDomainRequest
from openai_chatbot_domain.service.request.openai_chatbot_domain_tts_request import OpenaiChatbotDomainTTSRequest
from openai_chatbot_domain.service.response.openai_chatbot_domain_response import OpenaiChatbotDomainResponse
from openai_chatbot_domain.service.response.openai_chatbot_domain_tts_response import OpenaiChatbotDomainTTSResponse

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))

from custom_protocol.service.custom_protocol_service_impl import CustomProtocolServiceImpl
from response_generator.response_class_map import ResponseClassMap
from request_generator.request_class_map import RequestClassMap

from user_defined_protocol.protocol import UserDefinedProtocolNumber


class UserDefinedProtocolRegister:
    @staticmethod
    def registerDefaultUserDefinedProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        firstUserDefinedFunctionService = FudfServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            firstUserDefinedFunctionService.justForTest
        )

    @staticmethod
    def OpenaiChatbotDomainProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        openaiChatbotDomainService = OpenaiChatbotDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.MAKE_RECIPE,
            OpenaiChatbotDomainRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.MAKE_RECIPE,
            OpenaiChatbotDomainResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.MAKE_RECIPE,
            openaiChatbotDomainService.generateRecipe
        )

    @staticmethod
    def OpenaiChatbotDamainTTSProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        openaiChatbotDomainService = OpenaiChatbotDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.MAKE_AUDIO,
            OpenaiChatbotDomainTTSRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.MAKE_AUDIO,
            OpenaiChatbotDomainTTSResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.MAKE_AUDIO,
            openaiChatbotDomainService.getGeneratedVoice
        )

    @staticmethod
    def LangchainChatbotDomainProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        langchainChatbotDomainService = LangchainChatbotDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.MAKE_RECIPE_WITH_RETRIEVER,
            LangchainChatbotDomainRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.MAKE_RECIPE_WITH_RETRIEVER,
            LangchainChatbotDomainResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.MAKE_RECIPE_WITH_RETRIEVER,
            langchainChatbotDomainService.getGeneratedRecipe
        )

    @staticmethod
    def LangchainChatbotDomainGetFaissIndexProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        langchainChatbotDomainService = LangchainChatbotDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.MAKE_DOCS_FAISS_INDEX,
            LangchainChatbotDomainGetFaissRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.MAKE_DOCS_FAISS_INDEX,
            LangchainChatbotDomainGetFaissResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.MAKE_DOCS_FAISS_INDEX,
            langchainChatbotDomainService.getFaissIndex
        )

    @staticmethod
    def ChatLogDomainGetLogProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        chatLogDomainService = ChatLogDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_LOG,
            ChatLogDomainGetRequest
        )
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_LOG,
            ChatLogDomainGetResponse
        )
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_LOG,
            chatLogDomainService.getLog
        )

    @staticmethod
    def ChatLogDomainGetAllLogProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        chatLogDomainService = ChatLogDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_ALL_LOGS,
            ChatLogDomainGetAllRequest
        )
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_ALL_LOGS,
            ChatLogDomainGetAllResponse
        )
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_ALL_LOGS,
            chatLogDomainService.getAllLogs
        )

    @staticmethod
    def ChatLogDomainDeleteLogProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        chatLogDomainService = ChatLogDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.DELETE_LOG,
            ChatLogDomainDeleteRequest
        )
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.DELETE_LOG,
            ChatLogDomainDeleteResponse
        )
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.DELETE_LOG,
            chatLogDomainService.deleteLog
        )

    @staticmethod
    def ChatLogDomainSaveLogProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        chatLogDomainService = ChatLogDomainServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.SAVE_LOG,
            ChatLogDomainSaveRequest
        )
        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.SAVE_LOG,
            ChatLogDomainSaveResponse
        )
        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.SAVE_LOG,
            chatLogDomainService.saveLog
        )

    @staticmethod
    def registerUserDefinedProtocol():
        UserDefinedProtocolRegister.registerDefaultUserDefinedProtocol()
        UserDefinedProtocolRegister.OpenaiChatbotDomainProtocol()
        UserDefinedProtocolRegister.OpenaiChatbotDamainTTSProtocol()
        UserDefinedProtocolRegister.LangchainChatbotDomainProtocol()
        UserDefinedProtocolRegister.LangchainChatbotDomainGetFaissIndexProtocol()
        UserDefinedProtocolRegister.ChatLogDomainGetLogProtocol()
        UserDefinedProtocolRegister.ChatLogDomainGetAllLogProtocol()
        UserDefinedProtocolRegister.ChatLogDomainDeleteLogProtocol()
        UserDefinedProtocolRegister.ChatLogDomainSaveLogProtocol()
