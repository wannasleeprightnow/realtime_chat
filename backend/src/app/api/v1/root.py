from fastapi import APIRouter

from common.settings import get_settings
from .user import router as user_router

root_router = APIRouter(prefix=get_settings().app_settings.api_v1_prefix)
root_router.include_router(user_router)
