from uuid import UUID

from pydantic import BaseModel


class UserBaseScheme(BaseModel):
    id: UUID
    name: str


class UserCreateScheme(BaseModel):
    name: str
