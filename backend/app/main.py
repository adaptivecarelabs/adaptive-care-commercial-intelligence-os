from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="CIOS API",
    version="1.0.0",
    description="Commercial Intelligence Operating System API"
)

app.include_router(router)
