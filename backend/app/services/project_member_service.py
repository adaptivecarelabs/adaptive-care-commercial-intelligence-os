from sqlalchemy.orm import Session

from app.models.project_member import ProjectMember


class ProjectMemberService:
    def __init__(self, db: Session):
        self.db = db

    def add_member(
        self,
        project_id: int,
        user_id: int,
        role: str = "owner",
    ) -> ProjectMember:

        member = ProjectMember(
            project_id=project_id,
            user_id=user_id,
            role=role,
        )

        self.db.add(member)
        self.db.flush()

        return member

    def get_project_members(
        self,
        project_id: int,
    ):

        return (
            self.db.query(ProjectMember)
            .filter(ProjectMember.project_id == project_id)
            .all()
        )

    def is_member(
        self,
        project_id: int,
        user_id: int,
    ) -> bool:

        return (
            self.db.query(ProjectMember)
            .filter(
                ProjectMember.project_id == project_id,
                ProjectMember.user_id == user_id,
            )
            .first()
            is not None
        )

    def get_member_role(
        self,
        project_id: int,
        user_id: int,
    ):

        member = (
            self.db.query(ProjectMember)
            .filter(
                ProjectMember.project_id == project_id,
                ProjectMember.user_id == user_id,
            )
            .first()
        )

        if member is None:
            return None

        return member.role
