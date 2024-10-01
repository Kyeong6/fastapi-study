from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from database import context_get_conn

def execute_query(conn: Connection):
    query = "select * from blog"
    stmt = text(query)
    # SQL 호출하여 CursorResult 반환
    result = conn.execute(stmt)

    rows = result.fetchall()
    print(rows)
    result.close()

def execute_sleep(conn: Connection):
    query = "select sleep(5)"
    result = conn.execute(text(query))
    result.close()

for ind in range(20):
    try:
        # with문이니까 Cursur 반환도 작성 필요 x
        with context_get_conn() as conn:
            execute_sleep(conn)
            print("loop index:", ind)
    except SQLAlchemyError as e:
        print(e)
    finally:
        # conn.close()
        # print("connection is closed inside finally")
        pass


print("end of loop")