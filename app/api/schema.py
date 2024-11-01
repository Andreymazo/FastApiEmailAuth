# build a schema using pydantic
from pydantic import BaseModel, EmailStr
from datetime import datetime

class MessageSchema(BaseModel):
    title: str
    description: str
    user_id: int
    created_date: datetime
    time_updated: datetime

    class ConfigDict:
        orm_mode = True
        
class Message(MessageSchema):
    id: int

class UserSchema(BaseModel):
    parent_message_id:int
    name:str
    email:EmailStr
    created_date: datetime
    

class User(UserSchema):
    id: int
    
    class ConfigDict:
        orm_mode = True
        


# class NoteSchema(BaseModel):
#     title: str
#     description: str

# class NoteDB(NoteSchema):
#     id: int