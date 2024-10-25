from app.api.schema import MessageSchema
from app.db import message, database


async def post(payload: MessageSchema,):
    
    # user_id=
   
    query = message.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)