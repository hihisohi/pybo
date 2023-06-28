import datetime

from pydantic import BaseModel

# Question 스키마
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True
    # question_list() 리턴값인 _question_list는 딕셔너리가 아닌 Question 모델이기 때문에 Question 스키마로 자동 변환되지 않음 -> orm_mode를 True로 설정하면 Question 모델의 항목들이 자동으로 Question 스키마로 매핑됨!