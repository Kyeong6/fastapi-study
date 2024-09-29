## 비동기
- 주로 I/O Bound인 작업 처리에 효율적
  - 파일처리, 데이터베이스 처리, network 처리, 인고지능 inference

**클라이언트-서버 동기/비동기 처리**  
- 동기방식은 개별 client의 requesst 처리를 서버가 순차적으로 수행
- 비동기 방식은 먼저 들어온 client의 request 처리를 완료하지 않고도 다음 client의 request 처리를 받아들일 수 있음, 단 request내의 프로세스가 비동기일경우(async, await)

**async/await 키워드**  
- 비동기 함수 선언 시 async 키워드 사용
- 비동기 함수 호출 시 await 키워드 사용
- await는 async로 선언된 비동기 함수에서 수행

**언제 async를 사용할까?**  
- DB, file 처리할 때 async를 사용하는 것이 ThreadPool보다 일반적으로 성능이 좋음
- 특정 함수가 비동기(async)로 실행될 수 없는 상황이라면 ThreadPool(Multi-thread)방식으로 진행

**Async 여부에 따른 Event Loop와 ThreadPool 적용**  
- async def 수행 함수는 비동기 Event Loop를 적용
  - Main Thread에서 uvloop이 돌아가면서 비동기 방식이 진행
  - await가 있다면 callback 수행
- def 수행 함수는 ThreadPool(concurrency)을 적용

**FastAPI 비동기, 멀티 스레드, 멀티 프로세스**  
- FastAPI는 비동기, 멀티 스레드, 멀티 프로세스 방식 모두 제공
- 수행 함수의 async 적용시 동기 / 비동기 내부 로직에 따라 유의가 필요함
- 명령어 : uvicorn main:app --workers=4
  - 프로세스 4개

**Uvicorn, Starlette, FastAPI의 역할**  
- uvicorn(Java의 Tomcat과 비슷):
  - Python 기반의 ASGI(Asynchronous Server Gateway Interface) 웹서버, 비동기 프로그래밍에 초점
  - ASGI 서버는 HTTP(또는 Websocket) Request를 처리하는 웹서버의 역할을 수행함과 동시게 ASGI 규약을 준수하는 파이썬 애플리케이션을 구동, 비동기적 요청 처리로 많은 동시 접속을 효율적으로 처리
- Starlette:
  - ASGI 기반의 Lightweight, Framework/toolkit
  - 웹 애플리케이션 구현을 위한 많은 기반 컴포넌트 제공
  - Routing, middleware, Cookie 등 FastAPI에 사용되는 많은 기능들의 기반
- FastAPI:
  - 모던, 고성능 웹 Framework
  - 편리한 Request 처리, Pydantic 통합, Swagger 자동화 등의 기능으로 편리하게 구현 가능

**역할 수행**  
- 브라우저에서 요청을 보내면 Uvicorn이 먼저 Request 파싱 수행
- 이후 FastAPI 안에 존재하는 Starlette이 활용되고, Response를 Uvicorn이 전달