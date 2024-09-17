## Path parameter
- URL Path의 일부로서 **path 정보를 담아서 GET MEthod**로 전달
- 예를 들어, http://www.example.com/job/2 라면 2를 path request 값으로 전달하고 이를 API 서버에서 인식할 수 있음
- 메시지는 Body 없이 전달
- 설정 방법 : /job/{id}
- {id}일 경우 id에 따른 페이지 설정이 가능하겠네?

**메시지 예시**  
```GET/job2/HTTP1.1
Host: www.example.com
User-Agent: Mozilla
Accept: application/json
```


## Query Parameter
- Query String이라고 불리며 url에서 ?뒤에 key와 value 값을 가지는 형태로 GET Method로 request 전달. 
  - 개별 parameter는 &로 분리
- http://www.example.com/job?id=3&pageIndex=1&sort=ascending 이라면 변수명 id로 3, pageIndex로 1, sort는 ascending으로 값을 전달
- 메시지는 Body 없이 전달

**메시지 예시**  
```GET/job?id=3&pageIndex=1&sort=ascending
Host: www.example.com
User-Agent: Mozilla
Accept: application/json
```


## Request Body
- POST/PUT Method로 Message Header가 아닌 Body에 작성된 Request
  - 참고로 GET 메시지는 Body가 없고 blank line, POST/PUT 메시지는 blank line 뒤에 Body 존재
- FastAPI에서는 Content-type: application/json으로 전송되어 Body에 전송된 JSON 기반 Request 의미
- Content_Type에서 json인 것이 중요하다. application/json일 경우 Request Body 클래스가 이를 처리

**메시지 예시**  
```POST/items HTTP/1.1
Host: localhost:801
User-Agent: Mozilla
Accept: application/json
Content-Type: application/json

{"id" : "min", "password": "123"}
```

## Form
- HTML Form에서 POST Method로 Message Header가 아닌 Body에 작성된 Request
- FastAPI에서 Content-type: application/x-www-form-urlencoded으로 Body에 작성된 Request 의미

**메시지 예시**  
```Post/login HTPP/1.1
Host: localhost:801
User-Agent: Mozilla
Accept: application/json
Content-Type: application/x-www-form-urlencoded

id=min&password=123
```

## FastAPI의 Request Parameter 처리 Class들
- FastAPI는 Request parameter 처리 시 아래 class들을 활용하며, Pydantic 모델로 데이터 수록/변환/검증 수행
- 복잡한 검증 로직을 사용할 경우에는 Path, Query 클래스를 명시적으로 사용하지만, 그렇지 않을 경우에는 묵시적으로 처리

