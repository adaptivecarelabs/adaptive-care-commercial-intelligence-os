from sqlalchemy.orm import Session
from app.models.workspace import Workspace
from uuid import uuid4
from slugify import slugify


class WorkspaceService:

    def __init__(self, db: Session):
        self.db = db

    def create_workspace(
        self,
        name: str,
        slug: str,
    ) -> Workspace:

        workspace = Workspace(
            name=f"{name}'s Workspace",
            slug = f"{slugify(name)}-{uuid4().hex[:8]}"
        )

        self.db.add(workspace)
        self.db.flush()      # obtain workspace.id before commit

        return workspace

    def get_by_id(self, workspace_id: int):

        return (
            self.db.query(Workspace)
            .filter(Workspace.id == workspace_id)
            .first()
        )
    
    def get_by_slug(
        self,
        slug: str,
    ) -> Workspace | None:

        return (
            self.db.query(Workspace)
            .filter(Workspace.slug == slug)
            .first()
        )
