from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError
from app.auth.dependencies import get_current_user
from app.schemas.auth import RefreshTokenRequest

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService

from app.auth.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)

def register(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)

    existing_user = auth_service.get_user_by_email(payload.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    user = auth_service.create_user(
        email=payload.email,
        full_name=payload.full_name,
        password=payload.password,
    )

    return user

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)

    user = auth_service.authenticate(
        payload.email,
        payload.password,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return TokenResponse(
        access_token=create_access_token(str(user.id)),
        refresh_token=create_refresh_token(str(user.id)),
    )

@router.post(
    "/refresh",
    response_model=TokenResponse,
)
def refresh_token(
    payload: RefreshTokenRequest,
):
    try:
        decoded = decode_token(payload.refresh_token)

        if decoded.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )

        subject = decoded["sub"]

        return TokenResponse(
            access_token=create_access_token(subject),
            refresh_token=create_refresh_token(subject),
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )
    
@router.get("/me", response_model=UserResponse)
def me(
    current_user = Depends(get_current_user),
):
    return current_user
