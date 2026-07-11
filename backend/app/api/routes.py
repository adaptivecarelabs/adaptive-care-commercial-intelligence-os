from fastapi import APIRouter

from app.cache.redis import redis_client

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

    try:
        redis_client.ping()
    except Exception:
        redis_status = "unhealthy"

    return {
        "status": "healthy",
        "services": {
            "redis": redis_status,
        },
    }
