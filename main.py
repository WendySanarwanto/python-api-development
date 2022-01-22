from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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

# Finding post's index
def find_post_index(id: int):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
async def root():
    return {"message": "Hello FastAPI."}

@app.get("/posts")
async def get_posts():
    return { "data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
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
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: '{id}' was not found.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: '{id}' was not found."}
    return { "post_detail": post }

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    print(f"id: {id} type: {type(id)}")
    # Find index of Post by matched id
    index = find_post_index(id)
    print(f"index: {index} type(index): {type(index)}")
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: '{id}' does not exist.")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)