import uvicorn
from fastapi import FastAPI

from src.api.rest.api_v1.route_builder import build_routes
from src.modules.shared.logger import logger
from src.settings import APP_SETTINGS

app = FastAPI()
app = build_routes(app)


@app.get("/")
async def root():
    return {"message": "Hello from main server !"}


def start_server():
    port_no = APP_SETTINGS.API_PORT
    logger.info(f"Started server running on port: {port_no}")
    uvicorn.run(
        "src.api.main:app",
        port=int(port_no),
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    start_server()
