from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional, Dict, Any

class Project(BaseModel):
    id: UUID4
    name: str
    created_at: datetime
    updated_at: datetime

class DataSource(BaseModel):
    id: UUID4
    project_id: UUID4
    name: str
    type: str # Using str for simplicity, could be an Enum
    connection_details: Dict[str, Any]

class DataProfile(BaseModel):
    id: UUID4
    datasource_id: UUID4
    status: str # Enum: running, completed, failed
    results: Dict[str, Any]
    created_at: datetime

class CleansingRule(BaseModel):
    id: UUID4
    project_id: UUID4
    name: str
    description: Optional[str] = None
    implementation: Dict[str, Any]

class Mapping(BaseModel):
    id: UUID4
    project_id: UUID4
    source_datasource_id: UUID4
    target_datasource_id: UUID4
    mapping_details: Dict[str, Any]

class User(BaseModel):
    id: str # From Clerk
    organization_id: UUID4
    role: str # Enum: admin, editor, viewer
