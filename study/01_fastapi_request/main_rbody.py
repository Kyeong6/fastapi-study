# Request Body

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Annotated
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Pydantic Model 클래스는 반드시 BaseModel 클래스를 상속받아 생성
class Item(BaseModel):
    name: str
    # FastAPI는 타입 선정이 아주 중요 : 값이 안 들어올 경우 None이라는 것을 명시 
    description: str | None = None
    # 위의 코드는 python 3.10버전부터 가능
    # 아래 코드는 버전 상관없이 사용 : Optional
    # description: Optional[str] = None 
    price: float
    tax: float | None = None
    # tax: Optional[float] = None 

class User(BaseModel):
    username: str
    full_name: str | None = None

# 수행 함수의 인자로 Pydantic model이 입력되면 json 형태의 Request Body 처리
@app.post("/items/")
async def create_item(item: Item):
    return item

# Request Body의 Pydantic model 값을 Access하여 로직 처리
# 실제 프로젝트에서 많이 사용될 것 같은 개념
# 사용자가 입력을 했을 때 추가적인 key&value 반환
# python에서는 None이지만, json에서는 null -> 입력할 때 주의 
@app.post("/items_tax/")
async def create_item_tax(item: Item):
    item_dict = item.model_dump() # item.dict()가 deprecated됨
    # None일 수 있는 Optional한 필드이므로 조건문 사용
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# 여러 개의 request_body parameter 처리
# json 데이터의 이름값과 수행함수의 인자명 같아야 함
# Request body를 하면 application/json이므로 자동으로 json이 형성됨
# pydantic으로 설정한 값들이 자동으로 json이 형성된다는 의미
# user는 위의 Request Body의 user와 동일해야함
@app.put("/items_mt{item_id}")
async def update_item_mt(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


# Path, Query, Request Body 모두 함께 적용
# item_id : Path
# item : Request Body
# q : Query
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    # ** 은 key,value를 푼 것 
    # Request Body 같은 경우 json(dictionary) 형태이기때문에 풀 수 있다
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result