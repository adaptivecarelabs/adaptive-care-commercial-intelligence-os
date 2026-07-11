from sqlalchemy.orm import Session

from app.auth.security import hash_password, verify_password
from app.models.user import User


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def create_user(
        self,
        email: str,
        full_name: str,
        password: str,
    ):
        user = User(
            email=email,
            full_name=full_name,
            password_hash=hash_password(password),
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def authenticate(
        self,
        email: str,
        password: str,
    ):
        user = self.get_user_by_email(email)

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        return user
    
    def get_user_by_id(self, user_id: int):
    
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )
