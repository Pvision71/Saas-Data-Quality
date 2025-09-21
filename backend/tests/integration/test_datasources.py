import pytest
from fastapi.testclient import TestClient
from backend.src.main import app
import uuid

client = TestClient(app)

def test_create_datasource():
    project_id = uuid.uuid4()
    response = client.post(f"/projects/{project_id}/datasources", json={"name": "test", "type": "legacy_db"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "test"
    assert data["type"] == "legacy_db"