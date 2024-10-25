from fastapi import FastAPI
from app.api import ping, message, user
from app.db import engine, database, metadata
from contextlib import asynccontextmanager
metadata.create_all(engine)

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(ping.router)
app.include_router(message.router, prefix="/message", tags=["message"])
app.include_router(user.router, prefix="/user", tags=["user"])