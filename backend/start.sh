#!/bin/bash

alembic upgrade head
uvicorn web:create_app --factory --app-dir src/app/ --host=0.0.0.0 --port=8080 --reload