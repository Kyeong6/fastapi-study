from fastapi import APIRouter, Request
from db.database import direct_get_conn
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from schemas.blog_schema import BlogData

# router 생성
router = APIRouter(prefix="/blogs", tags=["blogs"])

# /blogs
@router.get("/")
# Request는 템플릿 엔진에서 사용
async def get_all_blogs(request: Request):
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
        conn.close()