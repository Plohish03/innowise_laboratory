from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base

class book (Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nulllable = False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

