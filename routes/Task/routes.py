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
def GetTask(id: str):
    return TaskService.get_task(id)


@TaskRouter.post("/")
def CreateTask(
    task: TaskModel = Body(embed=True),
):
    return TaskService.create_task(task)


@TaskRouter.put("/{id}")
def UpdateTask(id: str, task: TaskModel = Body(embed=True),):
    return TaskService.update_task(id, task)


@TaskRouter.delete("/{id}")
def DeleteTask(id: str):
    return TaskService.delete_task(id)
