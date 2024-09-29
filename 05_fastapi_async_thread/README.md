## 비동기
- 주로 I/O Bound인 작업 처리에 효율적
  - 파일처리, 데이터베이스 처리, network 처리, 인고지능 inference

**클라이언트-서버 동기/비동기 처리**  
- 동기방식은 개별 client의 requesst 처리를 서버가 순차적으로 수행
- 비동기 방식은 먼저 들어온 client의 request 처리를 완료하지 않고도 다음 client의 request 처리를 받아들일 수 있음, 단 request내의 프로세스가 비동기일경우(async, await)
