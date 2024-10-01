from fastapi import FastAPI
from routes.blog import router

app = FastAPI()

app.include_router(router)