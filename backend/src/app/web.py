from fastapi import FastAPI

from app.common.settings import settings
from app.depends import init_depends
from app.middlewares import init_middlewares
from app.routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings.app_settings.debug,
        title=settings.app_settings.title,
        docs_url=settings.app_settings.docs_url,
        openapi_url=settings.app_settings.openapi_url,
    )

    init_depends(app)
    init_routers(app)
    init_middlewares(app)

    return app
