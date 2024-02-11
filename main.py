from fastapi import FastAPI
from routers import user_router

app = FastAPI()

user = {
    "first_name": "John",
    "last_name": "Doe"
}
    
app.include_router(user_router)