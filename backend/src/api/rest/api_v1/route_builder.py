from fastapi import FastAPI

from src.api.rest.api_v1.products.routes import router as r_products


def build_routes(app: FastAPI) -> FastAPI:
    app.include_router(r_products, prefix="/v1")
    return app
