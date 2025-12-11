# This file defines the FastAPI app and all API endpoints.

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import Book
from schemas import BookCreate, BookOut

# Create database tables on startup if they do not exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Dependency that provides a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide the session to the request
    finally:
        db.close()  # Close session after request finishes


# ----------------------------
# CREATE BOOK
# ----------------------------
@app.post("/books/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book and save it to the database.
    """
    # Create ORM object from Pydantic data
    new_book = Book(**book.dict())

    # Add to session and save
    db.add(new_book)
    db.commit()
    db.refresh(new_book)  # Load generated ID

    return new_book


# ----------------------------
# GET ALL BOOKS
# ----------------------------
@app.get("/books/", response_model=list[BookOut])
def get_books(db: Session = Depends(get_db)):
    """
    Return a list of all books.
    If the table is empty, an empty list [] is returned.
    """
    books = db.query(Book).all()
    return books  # Always returns [], never 404


# ----------------------------
# DELETE BOOK BY ID
# ----------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by its ID.
    Returns a message whether the book exists or not.
    """
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        return {"message": "Book not found"}

    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


# ----------------------------
# UPDATE BOOK BY ID
# ----------------------------
@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, updated: BookCreate, db: Session = Depends(get_db)):
    """
    Update the title, author, or year of a book by ID.
    """
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        return {"message": "Book not found"}

    # Update fields
    for key, value in updated.dict().items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


# ----------------------------
# SEARCH BOOKS
# ----------------------------
@app.get("/books/search/", response_model=list[BookOut])
def search_books(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db)
):
    """
    Search for books by title, author, or year.
    Returns [] when nothing is found.
    """
    query = db.query(Book)

    # Apply filters only if provided
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year is not None:
        query = query.filter(Book.year == year)

    return query.all()  # Always returns [] when no matches
