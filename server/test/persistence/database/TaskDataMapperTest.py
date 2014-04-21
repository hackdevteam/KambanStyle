import unittest
from numpy.lib.function_base import select
from server.kamban.model.Task import Task
from server.persistence.database.TaskDataMapper import TaskDataMapper
from sqlite3 import connect

URL_DATABASE = "C:\\Users\Josue\Desktop\KanbanStyle.sqlite"


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mapper = TaskDataMapper()
        self.connection = connect(URL_DATABASE)
        self.connection.execute("INSERT INTO task (title, description, idc) VALUES (\'FirstTask\', \'FirstDescription\' ,3)")
        self.idt = self.connection.execute("SELECT idt FROM task WHERE title=\'FirstTask\'").fetchone()[0]
        self.connection.commit()

    def test_insert(self):
        mapper = TaskDataMapper()
        task_id = mapper.insert(Task("My Task", "My Description", 2))
        self.assertEqual("My Task", mapper.retrieve(task_id).get_title())

    def test_insert_return_id(self):
        self.assertIsNotNone(self.mapper.insert(Task("Other", "Description", 3)))

    def test_retrieve(self):
        mapper = TaskDataMapper()
        self.assertEqual("FirstTask", mapper.retrieve(self.idt).get_title())

    def test_update(self):
        mapper = TaskDataMapper()
        mapper.update("FirstTaskModified", "FirstDescriptionModified", 2, self.idt)
        self.assertEqual("FirstTaskModified", mapper.retrieve(self.idt).get_title())

    def tearDown(self):
        self.connection.execute('DELETE FROM task')
        self.connection.commit()
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
