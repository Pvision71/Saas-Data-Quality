from fastapi import FastAPI
from backend.src.api import projects, datasources

app = FastAPI()

app.include_router(projects.router)
app.include_router(datasources.router)
