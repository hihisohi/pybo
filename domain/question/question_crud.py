from models import Question
from sqlalchemy.orm import Session

# 질문 목록
def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list

# 질문 상세
def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question