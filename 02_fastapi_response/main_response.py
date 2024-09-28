from fastapi import FastAPI, status, Form
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    RedirectResponse
)
from pydantic import BaseModel

app = FastAPI()

# response_class는 default가 JSONResponse
# response_class는 엄격하게 작성은 필요 x
@app.get("/resp_json/{item_id}", response_class=JSONResponse)
def response_json(item_id: int, q: str | None = None):
    # status_code 기본값은 200
    return JSONResponse(content={"message": "Hello, World",
                                 "item_id": item_id,
                                 "q": q},
                                 status_code=status.HTTP_200_OK)

# HTML Response
@app.get("/resp_html/{item_id}", response_class=HTMLResponse)
def response_html(item_id: int, item_name: str | None = None):
    html_str = f'''
    <html>
    <body>
        <h2>HTML Response </h2>
        <p>item_id: {item_id}</p>
        <p>item_name: {item_name}</p>
    </body>
    </html>
    '''
    return HTMLResponse(content=html_str, status_code=status.HTTP_200_OK)

# Redirect(Get -> Get)
@app.get("/redirect")
async def redirect_only(comment: str | None = None):
    print(f"redirect {comment}")

    return RedirectResponse(url=f"/resp_html/3?item_name={comment}")

# Redirect(Post -> Get)
@app.post("/create_redirect")
def create_item(item_id: int = Form, item_name: str = Form()):
    print(f"item_id: {item_id} item_name:{item_name} has been created")

    # Post에서 Get으로 Method가 전환되는 redirect 시 status code가 302
    return RedirectResponse(url=f"/resp_html/{item_id}?item_name={item_name}",
                            status_code=status.HTTP_302_FOUND)