from app.api.schema import MessageSchema
from app.db import message, database


async def post(payload: MessageSchema,):
    
    # user_id=
   
    query = message.insert().values(title=payload.title, description=payload.description, created_date=payload.created_date, time_updated=payload.time_updated)
    return await database.execute(query=query)