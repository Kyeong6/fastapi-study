from pydantic import BaseModel, ValidationError, ConfigDict, Field, Strict
from typing import List, Optional, Annotated

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    # 문자열 -> 숫자값 자동 파싱을 허용하지 않을 경우 Strict 모드로 설정
    # Model 전체에 적용하려면 ConfigDict(strict=True) 설정
    # model_config = ConfigDict(strict=True)

    id: int
    name: str
    email: str
    addresses: List[Address] # 리스트로 가지고 있음, Address 값 addresses에 존재
    age: int | None = None 
    # age: Optional[int] = None

    # 개별 속성에 Strict 모드 설정 시 Field나 Annotated 이용. None 적용시 Optional
    
    # Field에 None은 Optional 적용
    # age: int = Field(None, strict=True)

    # Annotated은 = None으로 적용
    # age: Annotated[int, Strict()] = None

# Pydantic Model 객체화 시 자동으로 검증 수행 수행하고, 검증 오류 시 ValidationError raise
try:
    user = User(
        id=123,
        name="John",
        email="john@example.com",
        addresses=[{"street": "123", "city": "hometown", "country": "USA"}],
        age = "29" # 문자열 값을 자동으로 int로 파싱 -> pydantic 적용 
    )
    print(user)
except ValidationError as e:
    print(e)