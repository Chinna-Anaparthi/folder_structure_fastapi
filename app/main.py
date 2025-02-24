from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BookCreateModel(BaseModel):
    title:str   
    author:str

book = [
    {
        "id":1,
        "title":"think python",
        "author":"chinna"
    },
    {
        "id":2,
        "title":"think cython",
        "author":"chinna"
    }
]
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

@app.post("/app/{item}",status_code=201)
async def read_item(item:str):
    return {"message":f"hello {name}"}

@app.post("/api/create_book",status_code=201)
async def create_book(book_data:BookCreateModel):
    return {
        "title":book_data.title,
        "author":book_data.author
    }

@app.get("/app/books",status_code=201)
async def get_all_books():
    return book