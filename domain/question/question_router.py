from fastapi import APIRouter

from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question"
)

@router.get("/list")
# def question_list():
#     db = SessionLocal() # db세션 생성
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     db.close()  # 사용한 세션을 커넥션 풀에 반환 (세션을 종료하는 것이 아님!)
#     return _question_list

# 위 db = SessionLocal()과 db.close()는 반복되는 패턴이라 FastAPI의 Dependency Injection을 통해 아래와 같이 표현가능
def question_list():
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list