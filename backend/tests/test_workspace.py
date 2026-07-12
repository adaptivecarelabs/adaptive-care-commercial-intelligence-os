"""

"""

from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_my_workspace():
    
    email = f"{uuid4()}@example.com"
    
    register = client.post(
        "/auth/register",
        json={
            "email": email,
            "full_name": "Workspace Tester",
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
    access_token = login.json()["access_token"]

    response = client.get(
        "/workspaces/me",
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Workspace Tester's Workspace"
    assert data["slug"] == "workspace-tester"

    assert "id" in data
    assert "created_at" in data
