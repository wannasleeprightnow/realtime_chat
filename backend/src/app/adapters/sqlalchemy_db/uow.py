from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.adapters.sqlalchemy_db.repositories.user import SqlalUserRepository
from app.ports.uow import UoW


class SqlalUoW(UoW):
    def __init__(
        self,
        async_session_maker: async_sessionmaker[AsyncSession],
    ) -> None:
        self._session_factory = async_session_maker

    async def __aenter__(self) -> Self:
        self._session: AsyncSession = self._session_factory()

        self.users = SqlalUserRepository(self._session)
        return self

    async def __aexit__(self, *args: tuple) -> None:  # pyright: ignore[reportUnknownParameterType, reportMissingTypeArgument]
        await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
