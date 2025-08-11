from fastapi import FastAPI
import uvicorn
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
app = FastAPI()


@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'

# Define a simple in-memory database to store books
db: Dict[str, dict] = {}


class Book(BaseModel):
    name: str
    author: str
    price: float
    genre: str


@app.get("/api/book/{id}", response_model=Book)
def read_book(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    return db[id]


@app.put("/api/book/{id}", response_model=Book)
def update_book(id: str, book: Book):
    if id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    db[id].update(book.dict())
    return db[id]


@app.post("/api/book", response_model=Book)
def create_book(book: Book):
    id = str(len(db) + 1)
    db[id] = book.dict()
    return db[id]


@app.patch("/api/book/{id}", response_model=Book)
def partial_update_book(id: str, book: Book):
    if id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    db[id].update(book.dict(exclude_unset=True))
    return db[id]


@app.delete("/api/book/{id}")
def delete_book(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    del db[id]
    return {"message": "Book deleted successfully"}


@app.get("/api/books", response_model=Dict[str, Book])
def read_all_books():
    return db


@app.delete("/api/books")
def delete_all_books():
    db.clear()
    return {"message": "All books deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
