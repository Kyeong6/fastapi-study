## Python 기반에서 RDBMS 다루기
- DB 서버 자원 및 Client 애플리케이션의 안정적인 운영을 위해서는 Client 프로그램이 DB 서버에 접속하여 SQL을 전달하고, 결과를 반환할 때 발생하는 주요 메커니즘에 대한 이해가 반드시 필요

**SQL 수행을 위한 Client와 DB 서버간 주요 프로세스**  
- Client APP에는 DB Client Driver가 존재
- Client -> RDBMS
  1. DB Connection 요청(DB_URL)
  2. 생성된 Connection을 이용하여 SQL 요청
  3. Cursor에서 결과 데이터 fetch 요청(Cursor가 데이터를 가져옴)
  4. Connection 종료 요청
- RDBMS -> Client
  1. Client의 Connection을 위한 세션(DB기준 Connection 의미) 생성 및 Connection 허용
  2. 해당 SQL이 적절한 SQL인지 확인, SQL을 파싱하여 실행 계획 수립, SQL을 수행 후 결과르 반환할 수 있는 Cursor 생성
  3. Cursor에 결과를 fetch한 후 Client에게 전송
  4. 해당 Connection의 세션을종료, 세션이 점유한 자원도 같이 정리

**SQLAlchemy**  
- 서로 다른 Driver나, 서로 다른 RDBMS더라도 공통의 DB 처리 API를 기반으로 코드를 작성할 수 있게 해줌
- 많은 서드파티 솔루션들이 SQLAlchemy 지원
- connection을 engine으로 만들어서 먼저 engin을 생성
  - conn = engine.connect() 이런 형식