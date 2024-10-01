from pydantic import BaseModel, ValidationError, field_validator, model_validator
from typing import Optional

# 현업에서 가장 많이 사용하는 경우

class User(BaseModel):
    username: str
    password: str
    confirm_password: str


    # "   " -> None
    @field_validator('username')
    def username_must_not_be_empty(cls, value: str): # username의 값 : value
        if not value.strip():
            raise ValueError("Username must not be empty")
        return value
    
    @field_validator('password')
    def password_must_be_strong(cls, value: str):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        # isdigit()으로 0(문자) / 1(숫자) -> any()를 통해 or 개념 사용
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        # isalpha()으로 0(숫자) / 1(문자) -> any()를 통해 or 개념 사용
        if not any(char.isalpha() for char in value):
            raise ValueError("Password must contain at least one letter")
        
        # 결국 문자나 숫자를 모두 하나라도 포함시켜야 하는 로직
        return value
    
    # 비밀번호 재확인
    @model_validator(mode='after') # mode='after'는 개별 필드를 모두 검증하고 마지막에 모델 검증
    def check_password_match(cls, values):
        password = values.password
        confirm_password = values.confirm_password
        if password != confirm_password:
            raise ValueError("Password do not match")
        return values
    
# 검증 테스트
try:
    user = User(username="john_doe", password="Secret123", confirm_password="Secret123")
    print(user)
except ValidationError as e:
    print(e)