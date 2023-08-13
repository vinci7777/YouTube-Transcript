from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL

Base = declarative_base()

class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
