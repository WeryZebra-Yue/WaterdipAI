from fastapi import FastAPI, APIRouter
from routes.Example.controller import controllers
app = FastAPI()
ExampleRouter = APIRouter()


@ExampleRouter.get("/")
def ExampleController():
    return controllers.example()
