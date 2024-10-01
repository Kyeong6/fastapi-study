from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class User(BaseModel):
    # description, examples는 Swagger와 같은 문서 시스템에서 표시
    
    username: str = Field(..., description="The users's username", examples="john_doe")
    email: str = Field(..., description="The user's a email address", examples="john.doe@example.com")
    
    # min_length : 최소 글자 설정
    password: str = Field(..., min_length=8, description="The user's a password")

    # ge : 0보다 크거나 같고, le : 120보다 작거나 같음
    age: Optional[int] = Field(None, ge=0, le=120, description="The user's a age, must be between 0 and 120", examples=30)

    # 기본값 설정
    is_active: bool = Field(default=True, description="Is the user currently activte?", example=True)

# Example usage
try:
    # age는 Optional, is_activte 기본값 존재
    user = User(username="john_doe", email="john.doe@example.com", password="Secret123")
    print(user)
except ValidationError as e:
    print(e.json())


class Foo(BaseModel):
    positive: int = Field(gt=0) # greater than
    non_negative: int = Field(ge=0) # greater than or equal to
    negative: int = Field(lt=0) # less than
    non_positive: int = Field(le=0) # less than or equal to
    even: int = Field(multiple_of=2) # a multiple of the given number
    love_for_pydantic: float = Field(allow_inf_nan=True) # allow 'inf' '-inf' 'nan' values


foo = Foo(
    positive=1,
    non_negative=0,
    negative=-1,
    non_positive=0,
    even=2,
    love_for_pydantic=float('inf')
)
print(foo)

class Foo(BaseModel):
    short: str = Field(min_length=3)
    long: str = Field(max_length=10)
    regex: str = Field(pattern=r'^\d*$') # 문자열 정규 표현식(이메일 검증..)

foo = Foo(short='foo', long='foobarbaz', regex='123')
print(foo)


"""
max_digits: Decimal 최대 숫자수. 소수점 앞에 0만 있는 경우나, 소수점값의 맨 마지막 0은 포함 x
decimal_places: 소수점 자리수. 소수점 값의 맨 마지막 0은 포함 x
"""

from decimal import Decimal

class Foo(BaseModel):
    precise: Decimal = Field(max_digits=5, decimal_places=2)

foo = Foo(precise=Decimal('123.45'))
print(foo)