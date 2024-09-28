from fastapi import FastAPI

from common.settings import get_settings
from depends import init_depends
from middlewares import init_middlewares
from routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI(
        debug=get_settings().app_settings.debug,
        title=get_settings().app_settings.title,
        docs_url=get_settings().app_settings.docs_url,
        openapi_url=get_settings().app_settings.openapi_url,
    )

    init_depends(app)
    init_routers(app)
    init_middlewares(app)

    return app
