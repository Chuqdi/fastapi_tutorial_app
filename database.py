from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_PATH ="sqlite:///./database.db"

engine = create_engine(SQLALCHEMY_DATABASE_PATH, connect_args={
    "check_same_thread":False
})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)



def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()