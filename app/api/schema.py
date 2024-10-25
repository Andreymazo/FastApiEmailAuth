# build a schema using pydantic
from pydantic import BaseModel, EmailStr
from datetime import datetime

class MessageSchema(BaseModel):
    title: str
    description: str
    user_id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True
        
class Message(MessageSchema):
    id: int

class UserSchema(BaseModel):
    email:EmailStr
    age:int
    time_created: datetime
    time_updated: datetime

class User(UserSchema):
    id: int
    
    class Config:
        orm_mode = True
        
# from pydantic import BaseModel

# class NoteSchema(BaseModel):
#     title: str
#     description: str

# class NoteDB(NoteSchema):
#     id: int