from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import sessionmaker

from my_settings                import DATABASE


SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE['user']}:{DATABASE['password']}@127.0.0.1:5432/prism39"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
