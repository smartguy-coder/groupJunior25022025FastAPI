from fastapi import APIRouter, status
from applicatoins.users.schemas import RegisterUserFields, BaseFields, BaseFields

router_users = APIRouter()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    new_user: RegisterUserFields
) -> BaseFields:
    return new_user