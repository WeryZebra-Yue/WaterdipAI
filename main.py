from typing import Union
from fastapi import FastAPI
from common.routes import BaseRouter
app = FastAPI()
baseRoute = "/v1"
app.include_router(BaseRouter, prefix=baseRoute)


@app.get("/")
async def root():
    return {"message": "Hello World", "Docs": "https://waterdip.herokuapp.com/docs", "Base Route": "https://waterdip.herokuapp.com/v1"}
