from sqlalchemy.orm import Session

from app.models.workspace import Workspace


class WorkspaceService:
    def __init__(self, db: Session):
        self.db = db

    def create_workspace(
        self,
        name: str,
        slug: str,
    ) -> Workspace:

        workspace = Workspace(
            name=name,
            slug=slug,
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
