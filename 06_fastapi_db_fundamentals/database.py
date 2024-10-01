from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager

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

def direct_get_conn():
    try:
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(e)
        raise e
    
# with절 사용시 이슈
def context_get_conn():
    try:
        with engine.connect() as conn:
            # 바로 return 하면 안됨
            # yield를 사용하면 호출하는 쪽에서 제어를 가져감
            # 근데 yield를 사용하면 호출하는 쪽에서 next로 풀어줘야 함.. 그래서 잘 사용 x
            yield conn
    except SQLAlchemyError as e:
        print(e)
    finally:
        conn.close()
        print("Connection yield is finished")

# 잘 사용하는 방법: 호출하는 쪽에서 with문을 작성하고 databse.py에서는 다음과 같이 작성
# 의존성 주입할 때는 contextmanager 제거
@contextmanager
def context_get_conn():
    try:
        conn = engine.connect()
        # 호출하는 쪽에서 control 가져갈 수 있게 설정
        yield conn
    except SQLAlchemyError as e:
        print(e)
        raise e
    # finally는 옵션 사항, 하지만 여기서 작성하지 않으면 control하는 곳에서 작성 필요
    finally:
        conn.close()
        print("connection is closed inside finally")
        # pass
    