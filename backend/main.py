from fastapi import FastAPI
from ..backend.routes import task_routes, auth_routes

app = FastAPI()

app.include_router(task_routes)
app.include_router(auth_routes)