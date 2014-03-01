import unittest
from server.KanbanModel.Task import Task


class CreateTaskTest(unittest.TestCase):

    def test_create_task(self):
      task = Task("MyTitle", "Description of the task title")
      self.assertEqual("MyTitle", task.get_title())

    def test_get_description(self):
      task = Task("MyTitle", "Description of the task title")
      self.assertEqual("Description of the task title", task.get_description())

