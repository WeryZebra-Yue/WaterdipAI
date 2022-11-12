from fastapi import FastAPI, APIRouter
from routes.Task.controller import controllers
app = FastAPI()
TaskRouter = APIRouter()


@TaskRouter.get("/")
def ListTasks():
    return controllers.ListTasks()


@TaskRouter.get("/{id}")
def GetTask(id: str):
    return controllers.GetTask(id)


@TaskRouter.post("/")
def CreateTask():
    return controllers.CreateTask()


@TaskRouter.put("/{id}")
def UpdateTask(id: str):
    return controllers.UpdateTask(id)


@TaskRouter.delete("/{id}")
def DeleteTask(id: str):
    return controllers.DeleteTask(id)
