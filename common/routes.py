from fastapi import FastAPI, APIRouter
from routes.Task.routes import TaskRouter

app = FastAPI()

BaseRouter = APIRouter()
BaseRouter.include_router(TaskRouter, prefix="/tasks")
