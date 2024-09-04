from pymongo import MongoClient
import os
from urllib.parse import quote_plus  # URL 인코딩을 위한 모듈

# 환경 변수에서 MongoDB 인증 정보 가져오기
username = quote_plus(os.getenv('MONGO_INITDB_ROOT_USERNAME'))
password = quote_plus(os.getenv('MONGO_INITDB_ROOT_PASSWORD'))
db_name = 'lms_mongodb'
collection_name = 'mongo_recipe'

# MongoDB 연결 설정 (인증 정보 포함)
url = f'mongodb://{username}:{password}@mongodb-container:27017/{db_name}?authSource=admin'

def create_database_and_collection():
    client = MongoClient(url)

    # 데이터베이스 선택
    db = client[db_name]

    # 컬렉션이 없으면 생성
    if collection_name not in db.list_collection_names():
        print(f'Database "{db_name}" and Collection "{collection_name}" do not exist. Creating them now.')
        db.create_collection(collection_name)
        print(f'Database "{db_name}" and Collection "{collection_name}" created successfully.')
    else:
        print(f'Collection "{collection_name}" already exists in Database "{db_name}". Skipping creation.')

    client.close()

if __name__ == "__main__":
    create_database_and_collection()
