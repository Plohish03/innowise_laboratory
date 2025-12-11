# This file contains SQLAlchemy ORM models (database tables).

from sqlalchemy import Column, Integer, String
from database import Base

# Book table representation using SQLAlchemy ORM
class Book(Base):
    __tablename__ = "books"  # Name of the table in the database

    # Primary key that auto-increments
    id = Column(Integer, primary_key=True, index=True)

    # Title of the book (required)
    title = Column(String, nullable=False)

    # Author of the book (required)
    author = Column(String, nullable=False)

    # Year of publication (optional)
    year = Column(Integer, nullable=True)
