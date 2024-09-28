## HTTP Response

- HTTP Response는 client Request에 따른 server에서 내려 보내는 메시지
- 요청 Request의 처리 상태, 여러 메타 정보, 그리고 Content 데이터를 담고 있음

**메시지 예시**   
1. Status-Line(상태 라인): HTTP version과 Response 상태 코드, ex) 200 OK
2. Response Headers: Content type, 서버 정보 등의 다양한 메타 정보
3. Blank Line: Header와 Body를 구분
4. Response Body: HTML이나 JSON, Image 등의 client에게 전달되는 실질 데이터

**FastAPI Response Class 유형**  
- JSONResponse: JSON 타입 content 전송
  - Python object(dictionary format)을 json format으로 자동 변환
- HTMLResponse
- RedirectResponse: 요청 처리 후 다른 URL로 Client를 다른 URL로 Redirect하기 위해 사용
  - Server가 다른 Request를 다시 보내라고 Client에게 요청해서 Client가 다시 요청
- PlainTextResponse
- FileResponse: 파일을 다운로드하는데 주로 사용
- StreamingResponse: 대용량 파일의 Streaming이나 chat message 등에 사용
  