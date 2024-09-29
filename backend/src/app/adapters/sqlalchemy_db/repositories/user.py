from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.sqlalchemy_db.models.user import UserModel
from app.domain.models.user import User
from app.ports.repositories.user import UserRepository


class SqlalUserRepository(UserRepository):
    _model = UserModel

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_users_list(self) -> list[User]:
        query = select(self._model)
        result = await self._session.execute(query)
        return [user.read_model() for user in result.scalars().all()]

    async def insert_one_user(self, user: User) -> None:
        stmt = insert(self._model).values(user.to_dict())
        await self._session.execute(stmt)

    async def get_user_by_name(self, name: str) -> User | None:
        query = select(self._model).where(self._model.name == name)
        result = await self._session.execute(query)
        user = result.scalar_one_or_none()
        return user.read_model() if user else None
