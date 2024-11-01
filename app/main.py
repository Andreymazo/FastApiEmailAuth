from fastapi import FastAPI
from app.api import ping, message, user
from app.db import engine, database, metadata
from contextlib import asynccontextmanager
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, F

metadata.create_all(engine)

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    # await bot.set_webhook(url="ССЫЛКА С ВЕБХУКОМ",
    #                       allowed_updates=dp.resolve_used_update_types(),
    #                       drop_pending_updates=True)
    yield
    # await bot.delete_webhook()
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(ping.router)
app.include_router(message.router, prefix="/message", tags=["message"])
app.include_router(user.router, prefix="/user", tags=["user"])

bot = Bot(token="6193506005:AAHdqkSjhVCgRXHTPSHqdu8eadJpnR_2BKU", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
