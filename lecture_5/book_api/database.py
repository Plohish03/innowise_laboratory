# This file configures the database connection and SQLAlchemy setup.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Path to SQLite database file
DATABASE_URL = "sqlite:///./books.db"

# Create SQLAlchemy engine
# For SQLite + FastAPI we must use check_same_thread=False
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for defining ORM models
Base = declarative_base()
