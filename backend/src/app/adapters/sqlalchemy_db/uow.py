from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from ports.repositories.user import UserRepository
from ports.uow import UoW


class SqlalUoW(UoW):
    def __init__(
        self,
        async_session_maker: async_sessionmaker[AsyncSession],
        user_repository: UserRepository,
    ) -> None:
        self._session_factory = async_session_maker

        self.users: UserRepository = user_repository

    async def __aenter__(self) -> Self:
        self._session: AsyncSession = self._session_factory()
        return self

    @property
    def get_session(self) -> AsyncSession:
        return self._session

    async def __aexit__(self, *args: tuple) -> None:  # pyright: ignore[reportUnknownParameterType, reportMissingTypeArgument]
        await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
