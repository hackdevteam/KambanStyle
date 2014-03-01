import unittest
from server.test.CreateTaskTest import Task


class Column():
  def __init__(self, title):
    self.__title = title
    self.task_dictionary = {}

  def get_title(self):
    return self.__title

  def add(self, task):
    self.task_dictionary[task.get_title()] = task

  def get_task(self, task):
    return self.task_dictionary[task.get_title()]

  def get_tasks(self):
    return self.task_dictionary

  def remove(self, task_name):
    self.task_dictionary.__delitem__(task_name)


class ColumnTest(unittest.TestCase):
  def test_create_column(self):
    column = Column("MyTitle")
    self.assertEqual("MyTitle", column.get_title())

  def test_add_task_to_column(self):
    task = Task("MyTitle Task", "Description of the task title")
    column = Column("MyTitle Column")
    column.add(task)
    self.assertEqual("MyTitle Task", column.get_task(task).get_title())

  def test_remove_task_from_column(self):
    task = Task("MyTitle Task", "Description of the task title")
    column = Column("MyTitle Column")
    column.add(task)
    column.remove(task.get_title())
    self.assertEqual(0, len(column.get_tasks()))