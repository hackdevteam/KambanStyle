import unittest


class Task():
  def __init__(self, title, description):
    self.__title = title
    self.__description = description

  def get_title(self):
    return self.__title



class CreateTaskTest(unittest.TestCase):

    def test_create_task(self):
        task = Task("MyTitle", "Description of the task title")
        self.assertEqual("MyTitle", task.get_title())
