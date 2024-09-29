from functools import partial

from fastapi import FastAPI
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from adapters.sqlalchemy_db.repositories.user import SqlalUserRepository
from adapters.sqlalchemy_db.uow import SqlalUoW
from common.settings import PostgresSettings, get_settings
from ports.repositories.user import UserRepository
from ports.uow import UoW
from services.user import UserService


def create_async_sessionmaker(
    settings: PostgresSettings,
) -> async_sessionmaker[AsyncSession]:
    postgres_dsn: URL = URL.create(
        drivername="postgresql+asyncpg",
        username=settings.user,
        password=settings.password,
        host=settings.host,
        port=settings.port,
        database=settings.db,
    )

    async_engine: AsyncEngine = create_async_engine(
        url=postgres_dsn,
        echo=settings.echo,
        pool_size=settings.pool_size,
        max_overflow=settings.max_overflow,
    )
    return async_sessionmaker(async_engine, expire_on_commit=False)


def create_uow(
    async_session_maker: async_sessionmaker[AsyncSession],
    user_repository: UserRepository,
) -> SqlalUoW:
    return SqlalUoW(async_session_maker, user_repository)


def create_user_repository() -> UserRepository:
    return SqlalUserRepository()


def create_user_service() -> UserService:
    return UserService()


def init_depends(app: FastAPI) -> None:
    async_session_maker = create_async_sessionmaker(
        get_settings().postgres_settings
    )

    user_repository = create_user_repository()

    app.dependency_overrides[UoW] = partial(
        create_uow,
        async_session_maker,
        user_repository,
    )
    app.dependency_overrides[UserService] = create_user_service
