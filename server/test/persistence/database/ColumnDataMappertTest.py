import unittest
from server.kamban.model.Column import Column
from server.persistence.database.ColumnDataMapper import ColumnDataMapper
from sqlite3 import connect

URL_DATABASE = "C:\\Users\Josue\Desktop\KanbanStyle.sqlite"


class ColumnDataMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = ColumnDataMapper()
        self.connection = connect(URL_DATABASE)
        self.connection.execute("INSERT INTO column (title, idb) VALUES (\'FirstColumn\' ,3)")
        self.idc = self.connection.execute("SELECT idc FROM column WHERE title=\'FirstColumn\'").fetchone()[0]
        self.connection.commit()

    def test_insert(self):
        self.mapper.insert(Column("My Column", 2))
        self.assertEqual("My Column", self.mapper.retrieve("My Column").fetchone()[1])

    def test_retrieve(self):
        self.assertEqual("FirstColumn", self.mapper.retrieve("FirstColumn").get_title())

    def test_update(self):
        self.mapper.update('FirstColumnModified', 2, self.idc)
        self.assertEqual('FirstColumnModified', self.mapper.retrieve('FirstColumnModified').get_title())

    def tearDown(self):
        self.connection.execute('DELETE FROM column')
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
