import json

from server.kamban.model.Task import Task


class TaskApiEndPoint(object):
    exposed = True

    def __init__(self, persistence):
        self.__persistance = persistence

    def POST(self, title, description, column_id):
        task = Task(title, description, column_id)
        self.__persistance.save_task(task)
        return json.dumps({"title": task.get_title(), "description": task.get_description(), "task_id": task.get_id(),
                           "column_id": task.get_column_id()})
