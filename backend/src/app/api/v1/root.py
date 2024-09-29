from fastapi import APIRouter

from app.api.v1.user import router as user_router
from app.common.settings import settings

root_router = APIRouter(prefix=settings.app_settings.api_v1_prefix)
root_router.include_router(user_router)
