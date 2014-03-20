import json
from uuid import uuid4
from server.kamban.model.Task import Task


class TaskApiEndPoint(object):
    exposed = True

    def __init__(self, persistence):
        super.__persistance = persistence

    def POST(self, title, description):
        task = Task(title, description, str(uuid4()))
        self.__persistance.save(task)
        return json.dumps({"title": task.get_title(), "description": task.get_description(), "id": task.get_id(),
                           "column_id": task.get_column_id()})
