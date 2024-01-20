import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from fastapi_pagination.utils import disable_installed_extensions_check
from src.api.rest.api_v1.route_builder import build_routes
from src.modules.shared.logger import logger
from src.modules.shared.seed import read_and_seed_json
from src.settings import APP_SETTINGS

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app = build_routes(app)
add_pagination(app)
disable_installed_extensions_check()


@app.on_event("startup")
async def startup_event():
    await read_and_seed_json()


@app.get("/")
async def root():
    return {"message": "Hello from main server !"}


def start_server():
    api_port = APP_SETTINGS.API_PORT
    api_host = APP_SETTINGS.API_HOST
    logger.info(f"Started server running on port: {api_port}")
    uvicorn.run(
        "src.api.main:app",
        host=api_host,
        port=int(api_port),
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    start_server()
