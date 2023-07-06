import datetime

from pydantic import BaseModel, validator

class AnswerCreate(BaseModel):
    content: str

    @validator('content')   # AnswerCreate 스키마에 content값이 저장될때 실행
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

# 출력으로 사용할 답변 1개
class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True