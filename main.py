from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
async def get_data():
    return {"Message": "Hello world"}


@app.get("/greet")
async def get_name(Name:Optional[str]="User",Age:Optional[int]=18) -> dict:
    if Name and Age:
        return {"Message": f"Name is {Name}, Age is {Age}"}
    elif Name or Age:
        return {"Message": f"Name is {Name}, Age is {Age}"}
    

    
class Create_Book(BaseModel):
    title:str
    author:str
    
@app.post("/create_book")
async def create_book(book_data:Create_Book):
    return {
        "title":book_data.title,
        "author":book_data.author
    }
