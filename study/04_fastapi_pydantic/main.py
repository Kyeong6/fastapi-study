from fastapi import FastAPI, Path, Query, Form, Depends
from pydantic import BaseModel, Field, model_validator
from typing import Annotated
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    description: str = Field(None, max_length=500)
    price: float = Field(..., ge=0)
    tax: float = None

    @model_validator(mode='after')
    def tax_must_be_less_than_price(cls, values):
        price = values.price
        tax = values.tax
        if tax > price:
            raise ValueError("Tax must be less than price")
        
        return values
    
@app.put("/items/{item_id}")
# async def update_item(item_id: int, q: str, item: Item=None):
# 위와 동일하지만, 명확하게 표현 가능
async def update_item(item_id: int = Path(...), q: str = Query(...), item: Item=None):
    return {"item_id": item_id, "q": q, "item": item}

# Path, Query, Request Body(json)
# Path와 Query에 조건을 주고싶으면 아래와 같이 작성 가능, Field 적용과 동일한 방법
@app.put("/items_json/{item_id}")
async def update_item_json(
    item_id: int = Path(..., gt=0, title="The ID of the item to get"),
    q1: str = Query(None, max_length=50),
    q2: str = Query(None, max_length=3),
    item: Item = None
):
    return {"item_id": item_id, "q1": q1, "q2": q2, "item": item}