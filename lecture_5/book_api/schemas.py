# This file contains Pydantic schemas that define how data
# is validated and returned via the API.

from pydantic import BaseModel

# Base schema shared between create and output models
class BookBase(BaseModel):
    title: str      # Book title
    author: str     # Book author
    year: int | None = None  # Optional year of publication

# Schema for creating a new book (input only)
class BookCreate(BookBase):
    pass  # No extra fields needed

# Schema for outputting a book (includes ID)
class BookOut(BookBase):
    id: int  # Unique identifier of the book

    # Allows Pydantic to read SQLAlchemy ORM objects
    class Config:
        orm_mode = True
