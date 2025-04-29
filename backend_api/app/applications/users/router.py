from fastapi import APIRouter, status
from applications.users.schemas import RegisterUserFields, BaseFields
from settings import settings

router_users = APIRouter()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    new_user: RegisterUserFields
) -> BaseFields:
    print(settings.POSTGRES_DB, 6666666666666666666666)
    return new_user
