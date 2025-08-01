# app/database.py
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
DATABASE_URL = "sqlite:///queries.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the model for our log table
class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)
    case_type = Column(String, index=True)
    case_number = Column(String, index=True)
    case_year = Column(String, index=True)
    raw_response_html = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Function to create the database and table
def init_db():
    Base.metadata.create_all(bind=engine)

# Function to add a log entry
def log_query(db_session, case_type, case_number, case_year, raw_response_html):
    log_entry = QueryLog(
        case_type=case_type,
        case_number=case_number,
        case_year=case_year,
        raw_response_html=raw_response_html
    )
    db_session.add(log_entry)
    db_session.commit()
    db_session.close()