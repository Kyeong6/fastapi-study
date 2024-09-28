from fastapi import APIRouter
from pydantic import BaseModel

user_router = APIRouter(prefix="/users", tags=["users"])

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@user_router.get("/users/")
async def read_users():
    return [{"username": "ricky",
             "username": "martin"}]

@user_router.get("/users/me")
async def read_user_me():
    return {"username": "currentuser"}

@user_router.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}