from fastapi import APIRouter , status

router_users = APIRouter()


@router_users.post('/')
async def create_user():
    return{"st" : 200}
