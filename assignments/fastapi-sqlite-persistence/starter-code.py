import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books REST API")
DATABASE_PATH = Path(__file__).with_name("books.db")


class Book(BaseModel):
    id: int
    title: str
    author: str


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
            """
        )


initialize_database()


@app.get("/books")
def list_books():
    raise NotImplementedError("Read all books from SQLite")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    raise NotImplementedError("Read one book from SQLite")


@app.post("/books", status_code=201)
def create_book(book: Book):
    raise NotImplementedError("Insert a book into SQLite")


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    raise NotImplementedError("Update a book in SQLite")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    raise NotImplementedError("Delete a book from SQLite")