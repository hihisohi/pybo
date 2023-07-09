import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer

# Question 스키마
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []  # models에서 backref="answers"로 했으니까 answers라는 이름으로 연결해줘야함

    class Config:
        orm_mode = True
    # question_list() 리턴값인 _question_list는 딕셔너리가 아닌 Question 모델이기 때문에 Question 스키마로 자동 변환되지 않음 -> orm_mode를 True로 설정하면 Question 모델의 항목들이 자동으로 Question 스키마로 매핑됨!


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []