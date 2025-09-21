from backend.src.models.models import DataSource
import uuid

class DatasourceService:
    def create_datasource(self, project_id: uuid.UUID, name: str, type: str) -> DataSource:
        # This will be replaced with a database call
        return DataSource(
            id=uuid.uuid4(),
            project_id=project_id,
            name=name,
            type=type,
            connection_details={}
        )
