from pydantic import BaseModel, EmailStr, Field
# pip install email-validator tzdata

"""
EmailStr: Validate Email Address
"""

class UserEmail(BaseModel):
    # email: EmailStr # 문자열 Email 검증
    # email: EmailStr = Field(..., max_length=40) # Field와 함께 사용
    
    # 정규표현식
    email: EmailStr = Field(None, max_length=40, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

try:
    user_email = UserEmail(email="user@examples.com")
    print(user_email)
except ValueError as e:
    print(e)


"""
1. HttpUrl : http 또는 https만 허용, TLD(top-level domain)와 host명 필요
2. AnyUrl : https, https, ftp 등 어떤 프로토콜도 다 허용
3. AnyHttpUrl : http 또는 https만 허용, host명만 필요
4. FileUrl : 파일 프로토콜만 허용, host 명은 필요하지 않음
"""

from pydantic import HttpUrl, AnyUrl, AnyHttpUrl, FileUrl

class UserResource(BaseModel):
    http_url: HttpUrl
    any_url: AnyUrl
    any_http_url: AnyHttpUrl
    file_url: FileUrl

try:
    user_resource = UserResource(
        http_url="https://www.example.com",
        any_url="ftp://example.com",
        any_http_url="http://www.example.com",
        file_url="file:///path/to/file.txt"
    )
except ValueError as e:
    print(f"Value error: {e}")