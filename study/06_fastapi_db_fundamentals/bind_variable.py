from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from database import direct_get_conn
from datetime import datetime

try:
    # Connection 얻기
    conn = direct_get_conn()

    # SQL 선언 및 text로 감싸기
    # bind variable 표현은 :variable 사용
    query = "select id, title, author from blog where id = :id and author = :author \
        and modified_dt < :modified_dt"
    stmt = text(query)
    # :{variable}과 동일하게 parameter 설정
    # bind_variable을 통해서 코드상에서 값 가져올 수 있음
    bind_stmt = stmt.bindparams(id=1, author='둘리', modified_dt=datetime.now())

    result = conn.execute(bind_stmt)
    rows = result.fetchall()
    print(rows)
    result.close()
except SQLAlchemyError as e:
    print(e)
finally:
    conn.close()