from fastapi import FastAPI
from typing import Annotated

from pyexpat.errors import messages

app = FastAPI()

users = {"1": 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_user() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post_user(username:str, age:int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя:{username}, возраст:{age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id:int, username:str, age:int) -> str:
    users[user_id] = f'Имя:{username}, возраст:{age}'
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def del_user(user_id: str) -> str:
    users.pop(user_id)
    return  f"The user {user_id} is deleted"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)