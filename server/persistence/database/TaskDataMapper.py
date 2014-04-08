from server.kamban.model.Task import Task
from server.persistence.database.DataMapper import DataMapper


class TaskDataMapper(DataMapper):
    def __init__(self):
        DataMapper()

    def insert(self, task):
        self.query = "INSERT INTO task (title, description, idc) VALUES(?,?,?)"
        self.abstract_insert([task.get_title(), task.get_description(), task.get_column_id()])

    def retrieve_by_title(self, title):
        self.query = "SELECT * FROM task WHERE title=?"
        task_tuple = self.abstract_retrieve([title, ]).fetchone()
        return Task(task_tuple[1], task_tuple[2], task_tuple[3])

    def update(self, title, description, idc, idt):
        self.query = "UPDATE task SET title=?, description=?, idc=? WHERE idt=?"
        self.abstract_update([title, description, idc, idt])


