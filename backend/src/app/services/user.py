from sqlalchemy.exc import IntegrityError

from api.schemas.user import UserCreateScheme
from common.exceptions import UserAlreadyExistsError
from domain.models.user import User
from ports.uow import UoW


class UserService:
    async def get_users(self, uow: UoW) -> list[User]:
        async with uow:
            users = await uow.users.get_users_list(uow.get_session)
            return list(users)

    async def add_user(self, uow: UoW, user_data: UserCreateScheme) -> None:
        async with uow:
            try:
                await uow.users.insert_one_user(
                    uow.get_session, User(name=user_data.name)
                )
                await uow.commit()
            except IntegrityError as e:
                raise UserAlreadyExistsError from e
