from chat_log_domain.repository.chat_log_domain_repository_impl import ChatLogDomainRepositoryImpl
from chat_log_domain.service.chat_log_domain_service import ChatLogDomainService


class ChatLogDomainServiceImpl(ChatLogDomainService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__chatLogDomainRepository = ChatLogDomainRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    async def saveLog(self, account_id, recipe_hash, recipe):
        log_id = await self.__chatLogDomainRepository.saveLog(account_id, recipe_hash, recipe)
        return {'log_id': log_id}

    async def getAllLogs(self):
        return await self.__chatLogDomainRepository.getAllLogs()
