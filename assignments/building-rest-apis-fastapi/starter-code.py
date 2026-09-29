from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books REST API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    2: Book(id=2, title="Frankenstein", author="Mary Shelley"),
}


@app.get("/books")
def list_books():
    # TODO: Retorne todos os livros.
    raise NotImplementedError


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Retorne o livro solicitado ou gere HTTPException com status 404.
    raise NotImplementedError


@app.post("/books", status_code=201)
def create_book(book: Book):
    # TODO: Adicione o livro à coleção e retorne-o.
    raise NotImplementedError


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Substitua o livro correspondente ou gere HTTPException com status 404.
    raise NotImplementedError


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remova o livro correspondente ou gere HTTPException com status 404.
    raise NotImplementedError