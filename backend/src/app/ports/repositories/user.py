from abc import ABC, abstractmethod
from collections.abc import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    async def get_users_list(self, session: AsyncSession) -> Sequence[User]:
        raise NotImplementedError

    @abstractmethod
    async def insert_one_user(self, session: AsyncSession, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_name(
        self, session: AsyncSession, name: str
    ) -> User | None:
        raise NotImplementedError
