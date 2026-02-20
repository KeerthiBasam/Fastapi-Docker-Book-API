from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import schemas, crud

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "FastAPI Docker App Running"}

@app.post("/books")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books")
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)