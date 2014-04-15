import unittest
from sqlite3 import connect

from server.persistence.database.BoardURLDataMapper import BoardURLDataMapper


URL_DATABASE = "C:\\Users\Maca\Desktop\KanbanStyle.sqlite"

class BoardURLDataMapperTest(unittest.TestCase):
    def setUp(self):
        self.connection = connect(URL_DATABASE)
        self.connection.execute("INSERT INTO BoardURL (url, idb) VALUES (\'URLTest\',\'9\')")
        self.idb = self.connection.execute("SELECT idb FROM BoardURL WHERE url=\'URLTest\'").fetchone()[0]
        self.connection.commit()

    def test_retrieve_idb(self):
        mapper = BoardURLDataMapper()
        self.assertEqual(9, mapper.retrieve_idb("URLTest"))

    def test_insert_url(self):
        mapper = BoardURLDataMapper()
        mapper.insert("pepeTest2", "99")
        self.assertEqual(99, mapper.retrieve_idb("pepeTest2"))

    def tearDown(self):
        self.connection.execute('DELETE FROM BoardURL')
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
