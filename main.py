from typing import Union
from fastapi import FastAPI
from common.routes import BaseRouter
app = FastAPI()
baseRoute = "/v1"
app.include_router(BaseRouter, prefix=baseRoute)
