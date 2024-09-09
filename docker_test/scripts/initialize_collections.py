from pymongo import MongoClient, errors

# MongoDB 연결 설정
client = MongoClient("mongodb://username:password@localhost:27017/")
db = client['lms_mongodb']

# 데이터베이스와 컬렉션이 있는지 확인하고 없으면 생성
def initialize_collections():
    try:
        if 'lms_mongodb' not in client.list_database_names():
            print('Database "lms_mongodb" does not exist. Creating it.')
            db = client['lms_mongodb']

        # 메인 컬렉션 체크 및 생성
        if 'mongo_recipe' not in db.list_collection_names():
            print('Main collection "mongo_recipe" does not exist. Creating it.')
            db.create_collection('mongo_recipe')

        # 아카이브 컬렉션 체크 및 생성
        if 'mongo_recipe_archive' not in db.list_collection_names():
            print('Archive collection "mongo_recipe_archive" does not exist. Creating it.')
            db.create_collection('mongo_recipe_archive')

        print("Database and collections initialized successfully.")
    
    except errors.PyMongoError as e:
        print(f"MongoDB 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # DB 및 컬렉션 초기화 실행
    initialize_collections()
