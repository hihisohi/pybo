from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question"
)

@router.get("/list")
# 기본
# def question_list():
#     db = SessionLocal() # db세션 생성
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     db.close()  # 사용한 세션을 커넥션 풀에 반환 (세션을 종료하는 것이 아님!)
#     return _question_list

# db세션 생성, 반환 자동화 방법 1) get_db 제너레이터를 with과 함께 작성
# def question_list():
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list

# db세션 생성, 반환 자동화 방법 2) Depends 사용
def question_list(db: Session = Depends(get_db)):   # Depends는 매개 변수로 전달받은 함수의 실행결과를 리턴
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
# #Depends에서 contextmanager를 적용하므로 get_db에 적용한 어노테이션 제거 필요! 제거안하면 이중 적용으로 오류 발생