from fastapi import FastAPI, status
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    RedirectResponse
)
from pydantic import BaseModel

app = FastAPI()

# response_class는 default가 JSONResponse
@app.get("/resp_json/{item_id}", responses_class=JSONResponse)
def response_json(item_id: int, q: str | None = None):
    # status_code 기본값은 200
    return JSONResponse(content={"message": "Hello, World",
                                 "item_id": item_id,
                                 "q": q},
                                 status_code=status.HTTP_200_OK)