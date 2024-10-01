from sqlalchemy import create_engine, Connection
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from contextlib import contextmanager
from fastapi import status
from fastapi.exceptions import HTTPException


# database connection URL
DATABASE_CONN = "mysql+mysqlconnector://root:Root1234!@localhost:3306/blog_db"

engine = create_engine(DATABASE_CONN, #echo=True,
                       poolclass=QueuePool,
                       #poolclass=NullPool, # Connection Pool 사용하지 않음. 
                       pool_size=10, max_overflow=0,
                       pool_recycle=30)

def direct_get_conn():
    conn = None
    try:
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(e)
        raise e

# @contextmanager
def context_get_conn():
    # 견고하게 하기 위한 conn = None 작성
    conn = None
    try:
        conn = engine.connect()
        # control 하는쪽에 제어권 줌
        # return 해버리면 finally로 가서 connection close 됨
        yield conn
    except SQLAlchemyError as e:
        print(e)
        raise e
    finally:
        if conn:
            conn.close()