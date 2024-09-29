from abc import ABC, abstractmethod

from app.domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    async def get_users_list(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    async def insert_one_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_name(self, name: str) -> User | None:
        raise NotImplementedError
