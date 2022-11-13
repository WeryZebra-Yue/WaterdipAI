from common.db import db
from bson.objectid import ObjectId
from pydantic import BaseModel


class TaskService:
    def __init__(self) -> None:
        self.collection = db["tasks"]
        self.error_response = {
            "error": "There is no task at that id"
        }

    def list_task(self):
        tasks = list(self.collection.find())
        task_list = list(
            map(lambda x:  {"id": x["_id"].__str__(), **x}, tasks))
        return list(map(lambda x: {k: v for k, v in x.items() if k != "_id"}, task_list))

    def get_task(self, id: str):

        try:
            task = self.collection.find_one({"_id": ObjectId(id)})
        except:
            return self.error_response

        if(task):
            task_response = {
                "id": task["_id"].__str__(),
                **task
            }
            task_response.pop("_id")
            return task_response

        return self.error_response

    def create_task(self, task):
        task_id = self.collection.insert_one(task.dict()).inserted_id
        task_response = {
            "id": str(task_id),

        }
        return task_response

    def update_task(self, id: str, task: dict):
        try:
            task = self.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": task.dict()})
            print(task, id)
        except Exception as e:
            print(e)
            return self.error_response
        if task:
            return None

    def delete_task(self, id: str):
        try:
            task = self.collection.delete_one({"_id": ObjectId(id)})
        except:
            return None
        return None


TaskService = TaskService()
