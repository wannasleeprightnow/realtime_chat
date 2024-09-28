# ruff: noqa: ANN201
from abc import ABC, abstractmethod
from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession

from ports.repositories.user import UserRepository


class UoW(ABC):
    users: UserRepository

    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_session(self) -> AsyncSession:
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args: tuple) -> None:  # pyright: ignore
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
