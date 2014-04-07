import unittest
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
        mapper.insert(Task("My Task", "My Description", 2))
        self.assertEqual("My Task", mapper.retrieve_by_title("My Task").fetchone()[1])

    def test_retrieve(self):
        mapper = TaskDataMapper()
        self.assertEqual("FirstTask", mapper.retrieve_by_title("FirstTask").fetchone()[1])

    def test_update(self):
        mapper = TaskDataMapper()
        mapper.update("FirstTaskModified", "FirstDescriptionModified", 2, self.idt)
        self.assertEqual("FirstTaskModified", mapper.retrieve_by_title("FirstTaskModified").fetchone()[1])

    def tearDown(self):
        self.connection.execute('DELETE FROM task')
        self.connection.commit()
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
