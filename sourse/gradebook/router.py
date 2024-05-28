from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import STaskAdd, STask, STaskId
from repositiry import TasksRepo

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TasksRepo.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TasksRepo.find_all()
    return tasks
