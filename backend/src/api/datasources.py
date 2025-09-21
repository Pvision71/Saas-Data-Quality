from fastapi import APIRouter
from pydantic import BaseModel
from backend.src.models.models import DataSource
from backend.src.services.datasource_service import DatasourceService
import uuid

router = APIRouter()
datasource_service = DatasourceService()

class DataSourceCreate(BaseModel):
    name: str
    type: str

@router.post("/projects/{project_id}/datasources", response_model=DataSource, status_code=201)
def create_datasource(project_id: uuid.UUID, datasource: DataSourceCreate):
    return datasource_service.create_datasource(project_id=project_id, name=datasource.name, type=datasource.type)