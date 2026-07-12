from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.workspace import WorkspaceResponse
from app.services.workspace_service import WorkspaceService

router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"],
)

@router.get(
    "/me",
    response_model=WorkspaceResponse,
)
def get_my_workspace(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    workspace_service = WorkspaceService(db)

    workspace = workspace_service.get_by_id(
        current_user.workspace_id
    )

    return workspace
