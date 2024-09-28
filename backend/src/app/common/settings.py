from functools import lru_cache

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    title: str = "realtime_chat"
    debug: bool = False
    allow_origins: list[str]
    api_v1_prefix: str = "/api/v1"
    docs_url: str = "/api/docs"
    openapi_url: str = "/api/openapi.json"

    class Config:
        env_file = ".env"
        env_prefix = "app_"


class PostgresSettings(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    db: str

    echo: bool = False
    pool_size: int = 15
    max_overflow: int = 15

    class Config:
        env_file = ".env"
        env_prefix = "postgres_"
        case_sensetive = False


class AuthSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_prefix = "auth_"


class Settings:
    app_settings = AppSettings()  # type: ignore
    postgres_settings = PostgresSettings()  # type: ignore
    auth_settings = AuthSettings()  # type: ignore


@lru_cache
def get_settings() -> Settings:
    return Settings()
