from fastapi import APIRouter
from typing import List
from backend.src.models.models import Project
from backend.src.services.project_service import ProjectService

router = APIRouter()
project_service = ProjectService()

@router.get("/projects", response_model=List[Project])
def list_projects():
    return project_service.list_projects()
