from pymongo import MongoClient

# MongoDB 연결 설정
url = 'mongodb://localhost:27017'
db_name = 'your_database_name'
collection_name = 'your_collection_name'

def create_database_and_collection():
    client = MongoClient(url)
    
    # 데이터베이스 선택 (데이터베이스가 없으면 이 시점에서 생성됨)
    db = client[db_name]

    # 데이터베이스 생성(사실상 데이터베이스는 이 단계에서 MongoDB가 자동으로 생성함)
    # 이 부분은 데이터베이스가 명시적으로 생성되도록 하는 역할을 수행합니다.
    if collection_name not in db.list_collection_names():
        print(f'Database "{db_name}" and Collection "{collection_name}" do not exist. Creating them now.')
        db.create_collection(collection_name)
        print(f'Database "{db_name}" and Collection "{collection_name}" created successfully.')
    else:
        print(f'Collection "{collection_name}" already exists in Database "{db_name}". Skipping creation.')

    client.close()

if __name__ == "__main__":
    create_database_and_collection()
