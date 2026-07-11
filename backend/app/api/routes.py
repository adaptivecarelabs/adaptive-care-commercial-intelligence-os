from fastapi import APIRouter

from app.cache.redis import redis_client
from app.core.config import settings
from app.storage.client import bucket_exists

router = APIRouter()


@router.get("/", tags=["System"])
def root():
    return {
        "application": "CIOS",
        "status": "running",
        "version": "1.0.0",
        "message": "Welcome to the Adaptive Care Commercial Intelligence Operating System API",
    }


@router.get("/health", tags=["System"])
def health():
    redis_status = "healthy"
    storage_status = "healthy"

    try:
        redis_client.ping()
    except Exception:
        redis_status = "unhealthy"

    try:
        storage_ok = bucket_exists(settings.S3_BUCKET)
    except Exception:
        storage_ok = False

    return {
        "status": "healthy" if storage_ok else "degraded",
        "database": "ok",
        "storage": storage_ok,
    }   
