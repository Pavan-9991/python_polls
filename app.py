import datetime 

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

"""
username
email
created_at
updated_at
"""

class Users(BaseModel):
    username: str
    email:str
    created_at:datetime.datetime
    updated_at:datetime.datetime 


class Poll(BaseModel):
    title:str
    type :str
    is_add_choice_active:bool
    is_voting_active:bool
    created_by:int



@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/polls")
async def root():
    return{"polls":"Hello World"}


@app.get("/users")
async def root():
    return{"users":"Hello World"}


@app.post("/users/")
async def create_user(user: Users):
    return user

@app.post("/polls")
async def create_poll(poll: Poll):
    return poll

