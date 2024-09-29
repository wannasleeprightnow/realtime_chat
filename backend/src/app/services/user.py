from sqlalchemy.exc import IntegrityError

from app.api.schemas.user import UserCreateScheme
from app.common.exceptions import UserAlreadyExistsError
from app.domain.models.user import User
from app.ports.uow import UoW


class UserService:
    async def get_users(self, uow: UoW) -> list[User]:
        async with uow:
            users: list[User] = await uow.users.get_users_list()
            return users

    async def add_user(self, uow: UoW, user_data: UserCreateScheme) -> None:
        async with uow:
            try:
                await uow.users.insert_one_user(User(name=user_data.name))
                await uow.commit()
            except IntegrityError as e:
                raise UserAlreadyExistsError from e
