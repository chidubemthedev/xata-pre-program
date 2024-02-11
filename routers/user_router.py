from fastapi import APIRouter
from pydantic import BaseModel

user_router = APIRouter()

class User(BaseModel):
    first_name: str
    last_name: str

@user_router.post("/get-fullname/")
async def get_fullname(user: User):
    return {"fullname": f"{user.first_name} {user.last_name}"}