from common.db import db
from bson.objectid import ObjectId
from pydantic import BaseModel


class TaskService:
    def __init__(self) -> None:
        self.collection = db["tasks"]
        self.countCollection = db["count"]
        count = self.countCollection.find()
        self.count = list(count)[0]["count"]
        self.error_response = {
            "error": "There is no task at that id"
        }

    def update_count(self):
        self.countCollection.update_one(
            {"count": self.count}, {"$set": {"count": self.count + 1}})
        self.count += 1

    def list_task(self):
        tasks = list(self.collection.find())
        task_list = list(
            map(lambda x:  {"id": x["_id"].__str__(), **x}, tasks))
        return {"tasks": list(map(lambda x: {k: v for k, v in x.items() if k != "_id"}, task_list))}

    def get_task(self, id):

        try:
            task = self.collection.find_one({"id": id})
        except:
            return self.error_response

        if(task):

            task.pop("_id")
            return task

        return self.error_response

    def create_task(self, title, tasks):
        if title:
            # COUNT THE NUMBER OF TASKS

            task_count = self.count
            task_id = self.collection.insert_one({
                "id": task_count,
                "title": title,
                "is_completed": False
            }).inserted_id
            task_response = {
                "id": task_count,

            }
            self.update_count()

            return task_response
        if tasks:

            task_response = []
            for i in tasks:
                task_id = self.collection.insert_one({
                    "id": self.count,
                    "title": i.title,
                }).inserted_id
                self.update_count()

                task_response.append({
                    "id": self.count,
                })
            return task_response

            return task_response

    def update_task(self, id, task: dict):
        try:
            task = self.collection.update_one(
                {"id": id}, {"$set": task})
            print(task, id)
        except Exception as e:
            print(e)
            return self.error_response
        if task:
            return None

    def delete_task(self, id: int):
        try:
            task = self.collection.delete_one({"id": id})

        except:
            return None
        return None

    def delete_many(self, tasks):

        try:
            task = self.collection.delete_many(
                {"id": {"$in": list(map(lambda x: x, tasks))}})
        except:
            return None
        return None


TaskService = TaskService()
