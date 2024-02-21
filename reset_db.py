# reset_tables.py
from sqlalchemy import create_engine
from database.models import Base

DATABASE_URL = "sqlite:///database/test_db.db"

def reset_tables():
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    reset_tables()
