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
# engine = create_engine(DATABASE_CONN)
# echo=True는 SQL에 대한 상세한 정보(로그 느낌) 출력(트랜잭션, 롤백 ...)
engine = create_engine(DATABASE_CONN, echo=True,
                       # connection pool 생성
                       poolclass=QueuePool,
                       pool_size=10, max_overflow=0)
print("engine created")

# def direct_execute_sleep(is_close: bool = False):
#     # connection pooling해서 가져오는 connection임
#     conn = engine.connect()
#     query = "select sleep(5)"
#     result = conn.execute(text(query))
    
#     # 커서 닫기
#     result.close()

#     # 인자로 is_close가 True일 때만 connection close()
#     if is_close:
#         # connection pool로 돌아가는 것
#         conn.close()
#         print("conn closed")

# for ind in range(20):
#     print("loop index:", ind)
#     direct_execute_sleep(is_close=True)


# with 절 context를 이용한 DB connection 다루기
def context_execute_sleep():
    # with 절을 사용하면 conn.close()를 사용하지 않아도 자동으로 with문 빠져나가면 종료
    with engine.connect() as conn: # conn = engine.connect()과 동일
        query = "select sleep(5)"
        result = conn.execute(text(query))
        result.close()
        # conn.close()

for ind in range(20):
    print("loop index:", ind)
    context_execute_sleep()


print("end of loop")

"""
select * from sys.session where db='blog_db' order by conn_id;
수행하면 세션을 확인할 수 있는데 connection_id가 변하지 않음 -> 결국 connection pool을 새로 생성하는 것이 아닌
connection pool을 가져오고 반환하기 때문

만약 close(conn.close())가 되지 않았다면? Connection이 계속 만들어진다! 
낭비.. 
반드시 connection pool 종료가 필요하고, 제한하는 경우도 존재
"""