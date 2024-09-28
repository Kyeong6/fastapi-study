from fastapi import APIRouter
from pydantic import BaseModel

item_router = APIRouter(prefix="/item", tags=["item"])

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@item_router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@item_router.post("")
async def create_item(item: Item):
    return item

@item_router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id,
            "item": item}
