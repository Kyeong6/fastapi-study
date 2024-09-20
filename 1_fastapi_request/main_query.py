from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_item_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]

# http://localhost:8081/item?skip=0&limit=10
# 함수에 개별 인자값이 들어가 있는 경우 path parameter가 아닌 모든 인자는 query parameter
# query parameter의 타입과 default값을 함수 인자로 설정할 수 있음
# 만약 limit를 작성안한다면 자동으로 default 값인 10으로 설정
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # 인덱스
    return fake_item_db[skip : skip + limit]