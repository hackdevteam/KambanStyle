import unittest
from server.kamban.model.Task import Task


class TaskTest(unittest.TestCase):

	def test_create_task(self):
		task = Task("MyTitle", "Description of the task title", "column id")
		self.assertEqual("MyTitle", task.get_title())
		self.assertIsNotNone(task.get_id())

	def test_get_description(self):
		task = Task("MyTitle", "Description of the task title", "column id")
		self.assertEqual("Description of the task title", task.get_description())

