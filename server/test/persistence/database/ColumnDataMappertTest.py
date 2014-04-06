import unittest
from server.kamban.model.Column import Column
from server.persistence.database.ColumnDataMapper import ColumnDataMapper
from sqlite3 import connect

URL_DATABASE = "C:\\Users\Josue\Desktop\KanbanStyle.sqlite"


class ColumnDataMapperTest(unittest.TestCase):
    def setUp(self):
        self.connection = connect(URL_DATABASE)
        self.connection.execute("INSERT INTO column (title) VALUES (\'FirstColumn\')")
        self.idc = self.connection.execute("SELECT idc FROM column WHERE title=\'FirstColumn\'").fetchone()[0]
        self.connection.commit()

    def test_insert(self):
        mapper = ColumnDataMapper()
        mapper.insert(Column("My Column", 2))
        self.assertEqual("My Column", mapper.retrieve("My Column").fetchone()[1])

    def test_retrieve(self):
        mapper = ColumnDataMapper()
        self.assertEqual("FirstColumn", mapper.retrieve("FirstColumn").fetchone()[1])

    def test_update_title(self):
        mapper = ColumnDataMapper()
        mapper.update_title('FirstColumnModified', self.idc)
        self.assertEqual('FirstColumnModified', mapper.retrieve('FirstColumnModified').fetchone()[1])

    def tearDown(self):
        self.connection.execute('DELETE FROM column')
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
