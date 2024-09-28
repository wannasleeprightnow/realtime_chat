from abc import ABC, abstractmethod
from collections.abc import Sequence


class Repository[ModelT](ABC):
    @abstractmethod
    async def get_list(self) -> Sequence[ModelT]:
        raise NotImplementedError

    @abstractmethod
    async def insert_one(self, data: dict) -> None:  # type: ignore
        raise NotImplementedError
