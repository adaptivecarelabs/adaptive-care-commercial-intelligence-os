from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_project_creator_becomes_owner():

    email = f"{uuid4()}@example.com"

    register = client.post(
        "/auth/register",
        json={
            "email": email,
            "full_name": "Owner Test",
            "password": "password123",
        },
    )

    assert register.status_code == 201

    login = client.post(
        "/auth/login",
        json={
            "email": email,
            "password": "password123",
        },
    )

    assert login.status_code == 200

    token = login.json()["access_token"]

    project = client.post(
        "/projects",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "name": "RBAC Test Project",
            "description": "Testing owner membership",
        },
    )

    assert project.status_code == 201

    projects = client.get(
        "/projects",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert projects.status_code == 200
    assert len(projects.json()) >= 1
