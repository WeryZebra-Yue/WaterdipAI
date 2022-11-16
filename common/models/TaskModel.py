from pydantic import BaseModel
from typing import Union


class TaskModel(BaseModel):
    title:  Union[str, None] = None
    is_completed: Union[bool, None] = False
