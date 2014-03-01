import unittest


class Task(object):
  def __init__(self, title, description):
    self.__title = title
    self.__description = description

  def get_title(self):
    return self.__title

  def get_description(self):
    return self.__description



class CreateTaskTest(unittest.TestCase):

    def test_create_task(self):
      task = Task("MyTitle", "Description of the task title")
      self.assertEqual("MyTitle", task.get_title())

    def test_get_description(self):
      task = Task("MyTitle", "Description of the task title")
      self.assertEqual("Description of the task title", task.get_description())

