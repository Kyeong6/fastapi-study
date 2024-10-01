from fastapi import APIRouter, Request, Depends, status
from fastapi.exceptions import HTTPException
from db.database import direct_get_conn, context_get_conn
from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from schemas.blog_schema import BlogData

# router 생성
router = APIRouter(prefix="/blogs", tags=["blogs"])

# /blogs
@router.get("/")
# Request는 템플릿 엔진에서 사용
async def get_all_blogs(request: Request):
    conn = None
    try:
        conn = direct_get_conn()
        query = """
        SELECT id, title, author, content, image_loc, modified_dt FROM blog;
        """
        result = conn.execute(text(query))
        
        # 인덱스 혹은 row.id 이렇게 설정 가능
        # 아래 코드는 데이터 검증 진행 
        all_blogs = [BlogData(id=row[0],
              title=row[1],
              author=row[2],
              content=row[3],
              # DB와 Pydantic의 차이로 인한 500 에러 발생 
              image_loc=row[4],
              modified_dt=row[5]) for row in result]
        
        result.close()
        return all_blogs
    except SQLAlchemyError as e:
        print(e)
        raise e
    finally:
        # 중요
        if conn:
            conn.close()

@router.get("/show/{id}")
def get_blog_by_id(request: Request, id: int,
                   conn: Connection = Depends(context_get_conn)): # Depends를 통해서 해당 함수 불러줌
    try:
        query = """
        SELECT id, title, author, content, image_loc, modified_dt from blog
        where id = :id
        """
        stmt = text(query)
        # 첫번째 id는 query의 :id, 두번째 id는 path parameter id
        bind_stmt = stmt.bindparams(id=id)
        result = conn.execute(bind_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"해당 id {id}는 존재하지 않습니다.")
        
        row = result.fetchone()
        blog = BlogData(id=row[0], title=row[1], author=row[2], 
                 content=row[3], image_loc=row[4], modified_dt=row[5])
        result.close()

        return blog
    
    except SQLAlchemyError as e:
        print(e)
        raise e
    # 여기서 finally 안 해줘도 가능! 왜냐하면 context_get_conn()을 사용했기 때문