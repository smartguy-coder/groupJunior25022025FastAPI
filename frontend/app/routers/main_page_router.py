from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get('/')
async def index():
    return 'jkdfgdfhgfd'
