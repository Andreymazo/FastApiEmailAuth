from app.api import crud
from app.api.schema import User, UserSchema
from fastapi import APIRouter

router = APIRouter()

@router.post("/", response_model=User, status_code=201)
async def create_user(payload: UserSchema):
    user_id = await crud.post(payload)
    response_object = {
        "id": user_id,
        "email": payload.email,
        "age": payload.age,
    }
    return response_object