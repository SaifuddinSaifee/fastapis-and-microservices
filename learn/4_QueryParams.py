# PyDantic Base Model

from fastapi import FastAPI, HTTPException
from bookdb import book_database
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    yearPublished: int

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/books")
async def get_books(title: str | None = None, author: str | None = None, genre: str | None = None, yearPublished: int | None = None) -> list[dict]:
    books = book_database["books"]
    filtered_books = []
    for book in books:
        if title and book["title"].lower() != title.lower():
            continue
        if author and book["author"].lower() != author.lower():
            continue
        if genre and book["genre"].lower() != genre.lower():
            continue
        if yearPublished and book["yearPublished"] != yearPublished:
            continue
        filtered_books.append(book)
    books = filtered_books
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books
