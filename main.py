from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Post DTO with field's validation scheme
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# Global in-memory array
my_posts = [{ "id": 1, "title": "HOW TO - Creating CRUD API by using Fast API", "content": "TODO: Add more contents here."}, 
            { "id": 2, "title": "HOW TO - Buy your 1st Bitcoin.", "content": "Before buying your 1st Bitcoin, you should create a new account on CryptoExchange 1st like Binance."}]

# Finding post by id
def find_post(id: int):
    for post in my_posts:
        if post['id'] == id:
            return post

@app.get("/")
async def root():
    return {"message": "Hello FastAPI."}

@app.get("/posts")
async def get_posts():
    return { "data": my_posts}

@app.post("/posts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return { "data": post_dict}

@app.get("/posts/latest")
async def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
async def get_post(id: int):
    print(f"id: {id} type: {type(id)}")
    post = find_post(id)
    print(f"post: {post}")
    return { "post_detail": post }