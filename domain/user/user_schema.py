from pydantic import BaseModel, field_validator, EmailStr

class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr

    @field_validator('username', 'password1', 'password2', 'email')
    def not_emtpy(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @field_validator('password2')
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v