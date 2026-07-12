from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.auth.dependencies import get_current_user

from app.models.user import User

from app.schemas.project_member import (
    ProjectMemberCreate,
    ProjectMemberResponse,
)

from app.services.project_member_service import ProjectMemberService
from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/project-members",
    tags=["Project Members"],
)
