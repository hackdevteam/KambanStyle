import unittest
from server.KanbanModel.Column import Column
from server.KanbanModel.Task import Task


class ColumnTest(unittest.TestCase):
  def test_create_column(self):
    column = Column("MyTitle")
    self.assertEqual("MyTitle", column.get_title())

  def test_get_title_column(self):
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