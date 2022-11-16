from fastapi import FastAPI, APIRouter, Body, Response
from service.taskservice import TaskService
from common.models.TaskModel import TaskModel
from typing import Union

app = FastAPI()
TaskRouter = APIRouter()


@TaskRouter.get("/")
def ListTasks():
    return TaskService.list_task()


@TaskRouter.get("/{id}")
def GetTask(id: int):
    return TaskService.get_task(id)


@TaskRouter.post("/")
def CreateTask(
    tasks: Union[list[TaskModel], None] = Body(None),
    title: Union[str, None] = Body(None),
):
    return TaskService.create_task(title, tasks)


@TaskRouter.put("/{id}")
def UpdateTask(id: int, title: str = Body(embed=True), is_completed: bool = Body(embed=True)):
    print(id)
    return TaskService.update_task(id, {"title": title, "is_completed": is_completed})


@TaskRouter.delete("/{id}")
def DeleteTask(id: int):
    return TaskService.delete_task(id)


@TaskRouter.delete("/")
def DeleteTasks(tasks: Union[list, None] = None):
    return TaskService.delete_many(tasks)
