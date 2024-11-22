import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

@app.get("/")
async def root():
   return {"message": "hello world"}
class UserCreate(BaseModel):
    user_id: int
    username: str


@app.post("/create_user/")
async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    username = user_data.username
    return {
        "msg": "we got data succesfully",
        "user_id": user_id,
        "username": username,
    }


 


# To run locally
if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)
