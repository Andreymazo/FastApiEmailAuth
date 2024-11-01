import os
from fastapi import FastAPI
from app.api import ping, message, user
from app.db import DATABASE_URL, engine, database, metadata
from contextlib import asynccontextmanager
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram import Bot, Dispatcher, F
print(f'------------{DATABASE_URL}')
metadata.create_all(engine)

app = FastAPI()

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.api.utils import authenticate_user, get_current_user, get_db, get_user, verify_password, get_password_hash, create_access_token
from app.api.schema import User, TokenData
from app.db import SessionLocal, engine
from pydantic import EmailStr
from app.auth.routes import router as auth_router
from app.users.routes import router as users_router

SECRET_KEY=os.getenv('SECRET_KEY')

router = APIRouter()
# Base.metadata.create_all(bind=engine)
############## in utils.py ###############
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def get_user(db: Session, email: EmailStr):
#     return db.query(User).filter(User.email == email).first()

# def authenticate_user(db: Session, email: EmailStr, password: str):
#     user = get_user(db, email=email)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user

# def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         email: EmailStr = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#         token_data = TokenData(username=email)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(db, email=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


# #Такой подход не позволяет обращаться к ендпоинтам и творить логику (открыли и закрыли)
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await database.connect()
#     # await bot.set_webhook(url="ССЫЛКА С ВЕБХУКОМ",
#     #                       allowed_updates=dp.resolve_used_update_types(),
#     #                       drop_pending_updates=True)
#     yield
#     # await bot.delete_webhook()
#     await database.disconnect()

# app = FastAPI(lifespan=lifespan)





from app.api.schema import User as UserModel # User https://www.geeksforgeeks.org/authentication-and-authorization-with-fastapi/ определен через декларативбейс
@router.get("/me", response_model=User)
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user
# bot = Bot(token="6193506005:AAHdqkSjhVCgRXHTPSHqdu8eadJpnR_2BKU", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# dp = Dispatcher()


####################in users.routes.py############
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from app.api.schema import Token,User# UserResponse UserCreate
# from app.api.utils import get_password_hash 

# @router.post("/token", response_model=Token, tags=["token"])
# def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.post("/signup", response_model=User)
# def signup(user: User, db: Session = Depends(get_db)):
#     db_user = get_user(db, username=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     hashed_password = get_password_hash(user.hashed_password)
#     db_user = User(username=user.username, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


app.include_router(ping.router)
app.include_router(message.router, prefix="/message", tags=["message"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])