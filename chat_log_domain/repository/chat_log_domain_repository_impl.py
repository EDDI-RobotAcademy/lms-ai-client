from chat_log_domain.repository.chat_log_domain_repository import ChatLogDomainRepository

import os
from motor.motor_asyncio import AsyncIOMotorClient
import urllib.parse
from datetime import datetime

class ChatLogDomainRepositoryImpl(ChatLogDomainRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            return cls.__instance

    def __init__(self):
        connectionString = f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{urllib.parse.quote(os.getenv('MONGO_INITDB_ROOT_PASSWORD'))}@localhost:27017"
        dbName = os.getenv('MONGO_DB')
        self.__client = AsyncIOMotorClient(connectionString)
        self.__db = self.__client[dbName]
        self.__collection = self.__db['mongo_recipe']                  # 메인 컬렉션
        self.__archive_collection = self.__db['mongo_recipe_archive']  # 아카이브 컬렉션

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    async def saveLog(self, accountId: str, recipeHash: str, recipe: str):
        # 현재 시간을 lastAccessedAt에 추가
        log_data = {
            "account_id": accountId,
            "recipe_hash": recipeHash,
            "recipe": recipe,
            "lastAccessedAt": datetime.utcnow()  # 현재 UTC 시간 저장
        }

        # DB에 저장
        await self.__db_collection.insert_one(log_data)

    async def getAllLogs(self):
        return list(await self.__collection.find())

    async def deleteLogByAccountAndHash(self, account_id, recipe_hash):
        result = await self.__collection.delete_one({'account_id': account_id, 'recipe_hash': recipe_hash})
        return result.deleted_count

    async def getLogByAccountAndHash(self, accountId: str, recipeHash: str):
        # 1. Main DB에서 데이터 조회
        logData = await self.__db_collection.find_one({"account_id": accountId, "recipe_hash": recipeHash})
        
        if logData is not None:
            # 2. 조회 시 lastAccessedAt을 현재 시간으로 업데이트
            await self.__db_collection.update_one(
                {"account_id": accountId, "recipe_hash": recipeHash},
                {"$set": {"lastAccessedAt": datetime.utcnow()}}
            )
            return logData

        # 3. DB에 데이터가 없는 경우 -> 아카이브에서 조회
        logData = await self.getLogFromArchive(accountId, recipeHash)
        return logData
    
    async def getLogFromArchive(self, accountId, recipeHash):
        # 아카이브에서 해당 청크 조회 및 압축 해제
        archiveData = await self.__archive_collection.find_one({'chunk_id': 'some_chunk_id'})
        decompressedChunk = self.decompressDocument(archiveData['chunk'])

        # 해당 문서 찾기 및 나머지 문서 분리
        requestedLog = next((log for log in decompressedChunk if log['recipe_hash'] == recipeHash), None)
        remainingLogs = [log for log in decompressedChunk if log['recipe_hash'] != recipeHash]

        # 4. 해당 문서를 DB에 저장 및 lastAccessedAt 업데이트
        requestedLog['lastAccessedAt'] = datetime.utcnow()
        await self.__db_collection.insert_one(requestedLog)
        await self.__archive_collection.delete_one({'recipe_hash': recipeHash})

        # 5. 나머지 문서들을 재압축하여 아카이브에 저장 (비동기 처리)
        compressedRemaining = self.compressDocument(remainingLogs)
        await self.__archive_collection.insert_one({'chunk': compressedRemaining})

        return requestedLog
