from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from
import httpx

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get('/')
async def index(request: Request):
    context = {'request': request}
    response = templates.TemplateResponse('index.html', context=context)
    return response

async def login_user(user_email: str, password: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url='http://backend_api:9999/api/auth/login',
            data={"username": user_email, 'password': password}

        )
        print(response.json())
        return response.json()


async def get_user_info(access_token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url='http://backend_api:9999/api/auth/get-my-info',
            headers={"Authorization": f'Bearer {access_token}'}

        )
        print(response.json())
        return response.json()

async def get_current_user_with_token(request: Request) -> dict:
    access_token = request.cookies.get('access_token')
    if not access_token:
        return {}
    user = await get_user_info(access_token)
    user['access_token'] = access_token
    return user


@router.get('/login')
@router.post('/login')
async def login(request: Request, user: dict=Depends(get_current_user_with_token), user_email: str = Form(''), password: str = Form('')):
    context = {'request': request, 'user': user}
    if user:
        redirect_url = request.url_for("index")
        response =


    user_tokens = await login_user(user_email, password)
    access_token = user_tokens.get('access_token')
    user = None
    if access_token:
        user = await get_user_info(access_token)



    response = templates.TemplateResponse('login.html', context=context)
    response.set_cookie(key="access_token", value=access_token, httponly=True, max_age=60*5)
    return response
