from fastapi import APIRouter
from ..models.task import Task

router = APIRouter()

tasks = []

@router.get("/tasks")
async def get_tasks():
    return tasks

@router.post("/tasks")
async def create_task(task: Task):
    tasks.append(task)
    return task