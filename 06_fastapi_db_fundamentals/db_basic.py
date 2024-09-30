from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError

# database connection URL
"""
작성방법 
"DB+DB driver명://user:user_password@ldb주소:db_port/db명"
"""
DATABASE_CONN = "mysql+mysqlconnector://root:Root1234!@localhost:3306/blog_db"

# Engine 생성
engine = create_engine(DATABASE_CONN,
                       # connection pool 생성
                       poolclass=QueuePool,
                       pool_size=10, max_overflow=0)

# engine 생성 확인
print("created engine")


# 이후 과정은 try, except로 작성하는 것이 좋음: 수행이 안 되더라도 Connection 반환할 수 있게?
try:
    # Connection 열기
    conn = engine.connect()

    # SQL 선언 및 text로 감싸기
    query = "select id, title from blog"
    stmt = text(query)

    # SQL 호출하여 CursorResult 반환
    result = conn.execute(stmt)

    # fetchall을 통해서 result 모두 가져오기(리스트 형태)
    rows = result.fetchall()
    print(rows)

    # close() 메소드 호출하여 connection 반환
    result.close()

except SQLAlchemyError as e:
    print(e)
finally:
    # exception이 발생해도 close() 수행해야 함(중요)
    # pool이 존재해서 돌아갈 수 있음, 없다면 아예 종료가 됨
    print("closed connection")
    conn.close()