import uuid

from sqlalchemy.orm import Mapped, mapped_column

from domain.models.user import User
from .base import Base


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    def read_model(self) -> User:
        return User(
            id=self.id,
            name=self.name,
        )
