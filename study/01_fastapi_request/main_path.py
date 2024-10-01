from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# http://localhost:8081/items/3 : 명령어 uvicorn main_path:app --realod --port=8081

# path parameter : item_id
# 웹페이지 동적으로 변화가능, 즉 item_id에 따라 페이지 다르게 할 수 있음
@app.get("/items/{item_id}")
# 수행 함수 인자로 path parameter가 입력
# 함수 인자의 타입을 지정하여 path parameter 타입 지정(type check)
async def read_item(item_id: int):
    return {"item_id": item_id}


# Path parameter에 지정된 특정 값들만 원할 때는 Enum Class로 Path 유형 지정
# Enum class를 enum mixin으로 str을 확장하는 class로 만듦
# 결국 정해진 값 이외에는 에러를 발생
class ItemType(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"

# item_type의 값으로 small/medium/large만 가능
# @app.get("/items/type/{item_type}")
# async def get_item_type(item_type: ItemType):
#     return {"message": f"item type is {item_type}"}

# 추가적인 조건문 사용
@app.get("/items/type/{item_type}")
async def get_item_type(item_type: ItemType):
    if item_type is ItemType.small:
        return {"message": f"small item type should be very small {item_type}"}
    return {"message": f"item type is {item_type}"}