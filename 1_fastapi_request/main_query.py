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

# 함수 인자값에 default 값이 주어지지 않으면 반드시 query parameter에 해당하는 인자가 주어져야 함
@app.get("/items_id/")
async def read_item_id(skip: int, limit: int):
    return fake_item_db[skip : skip + limit]

# 함수 인자값에 default 값이 주어지지 않으면 None으로 설정
# None이 있을 경우 조건문을 작성해주자 : None에 대한 처리
# 추가적으로 Optional도 사용해보자!
@app.get("/items_op/")
async def read_item_op(skip: int, limit: Optional[int] = None):
    if limit:
       return fake_item_db[skip : skip + limit]
    else:
        return {"limit is not privided"}
    
# Path와 Query Parameter에 함께 사용
# decorator operator에서 자동으로 item_id를 Path Parameter로 인지
# 수행 함수 인자 중 item_id는 Path Parameter, 나머지는 모두 Query Paramter
# query parameter는 q=값 이런 형식으로 url 구성필요 
# bool 데이터 형식은 0 or 1로 작성
@app.get("/items/{item_id}")
async def read_item_path_query(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description" : "This is an amazing item that has a long description"}
        )
    return item