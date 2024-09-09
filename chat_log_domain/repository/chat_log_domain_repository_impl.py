from datetime import timedelta, datetime

from chat_log_domain.repository.chat_log_domain_repository import ChatLogDomainRepository

import os
from motor.motor_asyncio import AsyncIOMotorClient
import urllib.parse


class ChatLogDomainRepositoryImpl(ChatLogDomainRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            return cls.__instance

    def __init__(self):
        self.__expireAt = datetime.utcnow() + timedelta(days = 28)
        connectionString = f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{urllib.parse.quote(os.getenv('MONGO_INITDB_ROOT_PASSWORD'))}@localhost:27017"
        dbName = os.getenv('MONGO_DB')
        self.__client = AsyncIOMotorClient(connectionString)
        self.__db = self.__client[dbName]
        self.__collection = self.__db['mongo_recipe']

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    async def saveLog(self, account_id, recipe_hash, recipe):
        try:
            # 2419200 < 28일
            return await self.__collection.insert_one(
                {'account_id': account_id, 'recipe_hash': recipe_hash, 'recipe': recipe, 'expireAt': self.__expireAt})

        except Exception as e:
            print(f"error while saving: {e}")

    async def getAllLogs(self):
        return list(await self.__collection.find())

    async def deleteLogByAccountAndHash(self, account_id, recipe_hash):
        result = await self.__collection.delete_one({'account_id': account_id, 'recipe_hash': recipe_hash})
        return result.deleted_count

    async def getLogByAccountAndHash(self, account_id, recipe_hash):
        result = await self.__collection.find_one({'account_id': account_id, 'recipe_hash': recipe_hash})
        return result
