import uuid

from fastapi import APIRouter, Depends, status, HTTPException, Request, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from applications.users.crud import create_user_in_db, get_user_by_email, activate_user_account
from applications.users.schemas import BaseUserInfo, RegisterUserFields
from database.session_dependencies import get_async_session
from services.rabbit.constants import SupportedQueues
from services.rabbit.rabbitmq_service import rabbitmq_broker

router_payment = APIRouter()


