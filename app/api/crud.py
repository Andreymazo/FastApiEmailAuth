from app.api.schema import MessageSchema, UserSchema
from app.db import user, message, database


async def post_user(payload: UserSchema):
   
    query = user.insert().values(name=payload.name, parent_message_id=payload.parent_message_id, \
                                    email=payload.email, created_date=payload.created_date)
    return await database.execute(query=query)


async def post_message(payload: MessageSchema):
   
    query = message.insert().values(title=payload.title, description=payload.description, \
                                    created_date=payload.created_date, time_updated=payload.time_updated, user_id=payload.user_id)
    return await database.execute(query=query)

