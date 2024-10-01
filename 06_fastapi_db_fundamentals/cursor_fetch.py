from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from database import direct_get_conn

# FastAPI 프로젝트에서는 context_get_conn으로 진행, 연습이니까 실플하게 direct_get_conn을 사용
try:
    # Connection 얻기
    conn = direct_get_conn()

    # SQL 선언 및 text로 감싸기
    query = "select id, title from blog"
    stmt = text(query)

    # SQL 호출하여 CursorResult 반환
    result = conn.execute(stmt)
    # 개별 원소로 가지는 List로 반환
    rows = result.fetchall()

    # 단일 원소 반환
    # rows = result.fetchone() 

    # 개별 원소로 가지는 List로 반환(갯수만큼)
    # rows = result.fetchmany(2)

    # List Comprehension으로 rows Set을 개별 원소로 가지는 List로 반환
    # rows = [row for row in result]

    # 개별 row를 컬럼명을 key로 가지는 dict로 반환: Type이 dictionary
    # id 필드가 생겨서 자동 적용, 잘 사용하지 않음 메모리 꽤 잡아먹음
    # row_dict = result.mappings().fetchall()
    # print(row_dict)

    # 코드 레벨에서 컬럼명 명시화
    # row = result.fetchone()
    # print(row._key_to_index)
    # rows = [(row.id, row.title) for row in result]

    print(rows)
    # Cursor 반환
    result.close()

except SQLAlchemyError as e:
    print(e)

finally:
    conn.close()