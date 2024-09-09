import zlib
import json
from pymongo import MongoClient, errors
import datetime

# MongoDB 연결 설정
client = MongoClient("mongodb://username:password@localhost:27017/")
db = client['lms_mongodb']

# 메인 컬렉션과 아카이브 컬렉션
main_collection = db['mongo_recipe']
archive_collection = db['mongo_recipe_archive']

# 4주가 지난 문서들을 4개씩 청크로 압축하여 아카이브하는 함수
def archive_old_documents():
    four_weeks_ago = datetime.datetime.utcnow() - datetime.timedelta(weeks=4)
    
    try:
        # lastAccessedAt 필드 기준으로 4주가 지난 문서 찾기
        old_documents = list(main_collection.find({
            "lastAccessedAt": {"$lt": four_weeks_ago}
        }))

        # 4개씩 청크 단위로 압축 및 아카이브
        for i in range(0, len(old_documents), 4):
            chunk = old_documents[i:i+4]  # 4개씩 청크로 자름

            if chunk:
                # 압축하기 전, JSON 문자열로 변환
                chunk_data = json.dumps(chunk)
                # zlib을 이용하여 압축
                compressed_data = zlib.compress(chunk_data.encode('utf-8'))

                # 압축된 데이터를 아카이브 컬렉션에 저장
                archive_collection.insert_one({"compressed_data": compressed_data})

                # 원본 문서 삭제
                ids = [doc["_id"] for doc in chunk]
                main_collection.delete_many({"_id": {"$in": ids}})

                print(f"{len(chunk)}개의 문서를 압축하여 아카이브에 저장했습니다.")

    except errors.PyMongoError as e:
        print(f"MongoDB 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # 4주 지난 문서들을 아카이브
    archive_old_documents()
