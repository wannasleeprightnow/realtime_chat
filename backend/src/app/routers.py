from fastapi import FastAPI

from api.v1.root import root_router


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router)
