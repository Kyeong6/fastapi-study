from fastapi import FastAPI
from item import router

app = FastAPI()

app.include_router(router)