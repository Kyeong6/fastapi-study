from fastapi import FastAPI
from item import item_router
from user import user_router

app = FastAPI()

app.include_router(item_router)
app.include_router(user_router)