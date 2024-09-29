from typing import Annotated

from fastapi import APIRouter, Body, Depends

from app.api.schemas.user import UserBaseScheme, UserCreateScheme
from app.domain.models.user import User
from app.ports.uow import UoW
from app.services.user import UserService

router = APIRouter(prefix="/user")


@router.get("/", response_model=list[UserBaseScheme], status_code=200)
async def get_all_users(
    uow: Annotated[UoW, Depends()],
    service: Annotated[UserService, Depends()],
) -> list[User]:
    return await service.get_users(uow)


@router.post("/", response_model=None, status_code=201)
async def add_user(
    uow: Annotated[UoW, Depends()],
    service: Annotated[UserService, Depends()],
    user_data: Annotated[UserCreateScheme, Body()],
) -> None:
    await service.add_user(uow, user_data)
