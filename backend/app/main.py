from fastapi import FastAPI

from app.core.config import settings
from app.api.auth import router as auth_router
from app.api.routes import router as system_router
from app.api.workspaces import router as workspace_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

app.include_router(system_router)
app.include_router(auth_router)
app.include_router(workspace_router)
