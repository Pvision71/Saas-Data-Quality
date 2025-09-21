import pytest
from backend.src.services.project_service import ProjectService
from backend.src.services.datasource_service import DatasourceService
import uuid

def test_project_service_list_projects():
    service = ProjectService()
    projects = service.list_projects()
    assert isinstance(projects, list)
    assert len(projects) == 0

def test_datasource_service_create_datasource():
    service = DatasourceService()
    project_id = uuid.uuid4()
    datasource = service.create_datasource(project_id, "test_name", "test_type")
    assert datasource.project_id == project_id
    assert datasource.name == "test_name"
    assert datasource.type == "test_type"
    assert isinstance(datasource.id, uuid.UUID)
