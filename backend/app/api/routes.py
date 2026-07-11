from fastapi import APIRouter

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
    return {
        "status": "healthy"
    }
