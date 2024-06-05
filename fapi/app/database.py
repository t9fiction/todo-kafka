from sqlmodel import Session, SQLModel
from app.engine_file import engine


######################################################################

def get_db():
    with Session(engine) as session:
        print(session)
        yield session


######################################################################

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)