# build a schema using pydantic
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class MessageSchema(BaseModel):
    title: str
    description: str
    created_date: datetime
    time_updated: datetime
    user_id: int

    class ConfigDict:
        orm_mode = True
        
class Message(MessageSchema):
    id: int

class UserSchema(BaseModel):
    parent_message_id: Optional[int]=None
    name:str
    email:EmailStr
    created_date: datetime
    hashed_password: str

# class UserCreate(UserSchema):
#     password: str

class User(UserSchema):
    id: int
    
    class ConfigDict:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


# class NoteSchema(BaseModel):
#     title: str
#     description: str

# class NoteDB(NoteSchema):
#     id: int