from pydantic import BaseModel
from typing import Union


class TaskModel(BaseModel):
    title:  str
    is_completed: Union[bool, None] = False
