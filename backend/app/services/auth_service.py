from sqlalchemy.orm import Session

from app.auth.security import hash_password, verify_password
from app.models.user import User
from app.services.workspace_service import WorkspaceService
from app.utils.slug import generate_slug


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
        workspace_service = WorkspaceService(self.db)

        slug = generate_slug(full_name)

        workspace = workspace_service.create_workspace(
            name=full_name,
            slug=slug,
        )

        user = User(
            email=email,
            full_name=full_name,
            password_hash=hash_password(password),
            workspace_id=workspace.id,
        )

        try:
            self.db.add(user)

            self.db.commit()

            self.db.refresh(user)

            return user

        except Exception:
            self.db.rollback()
            raise

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
