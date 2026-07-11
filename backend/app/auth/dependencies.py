from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.auth.security import decode_token
from app.db.session import get_db
from app.services.auth_service import AuthService

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    try:
        payload = decode_token(credentials.credentials)

        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
            )

        user_id = int(payload["sub"])

        auth_service = AuthService(db)
        user = auth_service.get_user_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        auth_service = AuthService(db)

        user = auth_service.get_user_by_id(
            int(payload["sub"])
        )

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found",
        )

        return user
    
    

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
