from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from pydantic.dataclasses import dataclass

# class BlogInput(BaseModel):
#     title: str = Field(..., min_length=2, max_length=200)
#     author: str = Field(..., max_length=100)
#     content: str = Field(..., min_length=2, max_length=4000)
#     # 이미지 위치(path)
#     # DB와 Pydantic의 Null 차이
#     # 값이 None이 될 수 있을 경우에는 Optional 필수
#     # 여기서 고민해봐야할게 데이터베이스 값을 가져올 때 굳이 Pydantic을 해야할까? 
#     # 데이터베이스에는 애초에 테이블 생성할 때 데이터 타입 등을 설정함
#     image_loc: Optional[str] = Field(None, max_length=300)

# # 자동적으로 만들어짐
# class Blog(BlogInput):
#     id: int
#     modified_dt: datetime

# 위의 경우보다는 아래가 더 낫다고 생각
# @dataclass로 개발을 진행해보자
# @dataclass와 Pydantic으로 하면 반환값이 json 가능
@dataclass
class BlogData:
    id: int
    title: str
    author: str
    content: str
    modified_dt: datetime
    # None이 default값이면 맨 마지막에 위치 시키기
    # None 뒤에 있어버리면 나머지도 모두 None이 되버림
    image_loc: str | None = None

# @dataclass도 안하고 일반 객체도 가능
# 아래와 같은 일반 객체로 할 시 반환값 json x
# class BigData:
#     def __init__(self, id: int, title: str,
#                  author: str, content: str,
#                  image_loc: str, modified_dt: datetime):
        
#         self.id = id
#         self.title = title
#         self.author = author
#         self.content = content
#         self.image_loc = image_loc
#         self.modified_dt = modified_dt