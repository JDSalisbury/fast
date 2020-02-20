from .routers import basic, items, users
from fastapi import FastAPI
app = FastAPI()

app.include_router(basic.r, tags=["Test"])
app.include_router(items.r, tags=["Items"])
app.include_router(users.r, prefix="/users", tags=["Users"])
