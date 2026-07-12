from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_projects_route_exists():
    response = client.get("/projects")
    assert response.status_code in (401, 403)
