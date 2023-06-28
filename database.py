import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"    # 이 URL은 sqlite3이라는 db파일을 프로젝트 루트 디렉터리에 저장한다는 의미

# 커넥션 풀 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal : 데이터 베이스에 접속하기 위한 클래스, 추후 이 클래스로 생성한 db세션 객체를 사용한다.
# autocommit이 True이면 커밋하지 않아도 즉시 db에 변경사항이 적용되므로 rollback이 되지 않으니 주의!

# 데이터베이스 모델 구성
Base = declarative_base()

# Dependency Injection (의존성 주입)
def get_db():   # db 세션 객체를 리턴하는 제너레이터
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # with문을 벗어나는 순간 오류여부와 관계없이 db.close()가 실행되므로 보다 안전한 코드가 됨

