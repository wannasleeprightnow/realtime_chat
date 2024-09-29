from fastapi import APIRouter

from api.v1.user import router as user_router
from common.settings import get_settings

root_router = APIRouter(prefix=get_settings().app_settings.api_v1_prefix)
root_router.include_router(user_router)
