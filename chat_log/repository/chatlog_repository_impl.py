# repository/chatlog_repository_impl.py
from pymongo import MongoClient
from chat_log.repository.chatlog_repository import ChatlogRepository
import os

class ChatlogRepositoryImpl(ChatlogRepository):
    def __init__(self):
        connection_string = f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@localhost:27017/"
        db_name = os.getenv('MONGO_DB')
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db['chatlog']

    def save_log(self, log_data: dict):
        result = self.collection.insert_one(log_data)
        return str(result.inserted_id)

    def get_log_by_account_and_hash(self, account_id: str, recipe_hash: str):
        result = self.collection.find_one({'account_id': account_id, 'recipe_hash': recipe_hash})
        return result

    def delete_log_by_account_and_hash(self, account_id: str, recipe_hash: str):
        result = self.collection.delete_one({'account_id': account_id, 'recipe_hash': recipe_hash})
        return result.deleted_count

    def get_all_logs(self):
        return list(self.collection.find())
