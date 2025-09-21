import pytest
from fastapi.testclient import TestClient
from backend.src.main import app

client = TestClient(app)

def test_get_projects_empty():
    response = client.get("/projects")
    assert response.status_code == 200
    assert response.json() == []