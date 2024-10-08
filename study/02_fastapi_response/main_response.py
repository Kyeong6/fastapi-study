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

    # 다른 url로 이동시켜줌
    # 기본 status code는 307(Temporary Redirect)
    return RedirectResponse(url=f"/resp_html/3?item_name={comment}")

# Redirect(Post -> Get) : 제일 많이 쓰는 방식
# 로그인(post) 후 메인 페이지(get)로 이동할 경우
@app.post("/create_redirect")
def create_item(item_id: int = Form, item_name: str = Form()):
    print(f"item_id: {item_id} item_name:{item_name} has been created")

    # Post에서 Get으로 Method가 전환되는 redirect 시 status code가 302(Method 변경되었다는 의미)
    # Post -> Get일 경우 status code default인 307이 아닌 302로 설정해줘야 함
    # 다른 url로 이동시켜줌
    return RedirectResponse(url=f"/resp_html/{item_id}?item_name={item_name}",
                            status_code=status.HTTP_302_FOUND)


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None

class ItemResp(BaseModel):
    name: str
    description: str
    price_with_tax: float

# response model
@app.post("/create_item/", response_model=ItemResp,
          status_code=status.HTTP_201_CREATED)
async def create_item_rmodel(item: Item):
    if item.tax:
        price_with_tax = item.price + item.tax
    else:
        price_with_tax = item.price

    # response model을 통해서 답변 타입 타이트하게 설정 가능
    item_resp = ItemResp(
        name=item.name,
        description=item.description,
        price_with_tax=price_with_tax
    )
    return item_resp