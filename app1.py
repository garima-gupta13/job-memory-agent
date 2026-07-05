from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price : float
    tax: float | None = None
  
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Job Memory Agent is running"}


@app.get("/user/me")
async def get_user_me():
    return {"user": "current user"}

@app.get("/user/{user_id}")
async def get_user_by_id(user_id : str):
    return {"user_id" : user_id}


@app.post("/items/")
async def create_item(item : Item):
    return item