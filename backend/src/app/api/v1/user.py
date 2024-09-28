from typing import Annotated

from domain.models.user import User
from fastapi import APIRouter, Depends
from ports.uow import UoW
from services.user import UserService

from ..schemas.user import UserBaseScheme, UserCreateScheme

router = APIRouter(prefix="/user")


@router.get("/", response_model=list[UserBaseScheme], status_code=200)
async def get_all_users(
    uow: Annotated[UoW, Depends()],
    service: Annotated[UserService, Depends()],
) -> list[User]:
    return await service.get_users(uow)


@router.post("/", response_model=None, status_code=201)
async def add_user(
    user_data: UserCreateScheme,
    uow: Annotated[UoW, Depends()],
    service: Annotated[UserService, Depends()],
) -> None:
    await service.add_user(uow, user_data)
