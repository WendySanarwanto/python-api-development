from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello FastAPI."}

@app.get("/posts")
async def get_posts():
    return {"title": "HOW TO - Creating CRUD API by using Fast API", "content": "TODO: Add more contents here."}

@app.post("/posts")
async def create_posts(newPost: Post):
    print(newPost)
    return { "data": newPost}