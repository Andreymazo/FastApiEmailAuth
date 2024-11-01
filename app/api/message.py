from app.api import crud
from app.api.schema import Message, MessageSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/", response_model=Message, status_code=201)
async def create_message(payload: MessageSchema):
    message_id = await crud.post_message(payload)
    response_object = {
        "id": message_id,
        "title": payload.title,
        "description": payload.description,
        "created_date": payload.created_date,
        "time_updated": payload.time_updated,
        "user_id": payload.user_id
    }
    return response_object