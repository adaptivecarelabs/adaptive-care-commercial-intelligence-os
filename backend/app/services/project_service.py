from sqlalchemy.orm import Session

from app.models.project import Project
from app.services.project_member_service import ProjectMemberService


class ProjectService:
    def __init__(self, db: Session):
        self.db = db

    def create_project(
        self,
        workspace_id: int,
        user_id: int,
        name: str,
        description: str | None = None,
    ) -> Project:

        project = Project(
            workspace_id=workspace_id,
            name=name,
            description=description,
        )

        self.db.add(project)
        self.db.flush()

        member_service = ProjectMemberService(self.db)

        member_service.add_member(
            project_id=project.id,
            user_id=user_id,
            role="owner",
        )

        self.db.commit()
        self.db.refresh(project)

        return project
    
    def get_projects(
            self,
            workspace_id: int,
    ):
        return (
            self.db.query(Project)
            .filter(Project.workspace_id == workspace_id)
            .order_by(Project.created_at.desc())
            .all()
        )

    def get_by_id(
        self,
        project_id: int,
        workspace_id: int,
    ) -> Project | None:

        return (
            self.db.query(Project)
            .filter(
                Project.id == project_id,
                Project.workspace_id == workspace_id,
            )
            .first()
        )

