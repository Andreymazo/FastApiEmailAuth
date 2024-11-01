from app.api import crud
from app.api.schema import User, UserSchema
from fastapi import APIRouter

router = APIRouter()

@router.post("/", response_model=User, status_code=201)
async def create_user(payload: UserSchema):
    user_id = await crud.post_user(payload)
    response_object = {
        "id": user_id,
        "email": payload.email,
        "name": payload.name,
        "hashed_password":payload.hashed_password,
        "created_date":payload.created_date
    }
    return response_object