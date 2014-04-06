import unittest
from server.kamban.model.Task import Task
from server.persistence.database.TaskDataMapper import TaskDataMapper


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        mapper = TaskDataMapper()
        mapper.insert(Task("My Task", "My Description", 2))
        self.assertEqual("My Task", mapper.retrieve_by_title("My Task").fetchone()[1])

    def test_retrieve(self):
        mapper = TaskDataMapper()
        self.assertEqual("FirstTask", mapper.retrieve_by_title("FirstTask").fetchone()[1])


if __name__ == '__main__':
    unittest.main()
