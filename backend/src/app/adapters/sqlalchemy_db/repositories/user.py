from collections.abc import Sequence

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.sqlalchemy_db.models.user import UserModel
from domain.models.user import User
from ports.repositories.user import UserRepository


class SqlalUserRepository(UserRepository):
    _model = UserModel

    async def get_users_list(self, session: AsyncSession) -> Sequence[User]:
        query = select(self._model)
        result = await session.execute(query)
        return [user.read_model() for user in result.scalars().all()]

    async def insert_one_user(self, session: AsyncSession, user: User) -> None:
        stmt = insert(self._model).values(user.to_dict())
        await session.execute(stmt)

    async def get_user_by_name(
        self, session: AsyncSession, name: str
    ) -> User | None:
        query = select(self._model).where(self._model.name == name)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        return user.read_model() if user else None
