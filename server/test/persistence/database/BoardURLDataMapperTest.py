import unittest
from sqlite3 import connect
from server.persistence.database.DataMapper import DataMapper

URL_DATABASE = "C:\\Users\Maca\Desktop\KanbanStyle.sqlite"


class BoardURLDataMapper(DataMapper):
    def __init__(self):
        DataMapper()

    def insert(self, url, id_board):
        self.query = "INSERT INTO BoardURL (title, idb) VALUES(?,?)"
        return self.abstract_insert(url, id_board)

    def retrieve_idb(self, url):
        self.query = "SELECT idb FROM BoardURL WHERE url=?"
        return self.abstract_retrieve([url, ]).fetchone()[0]


class BoardURLDataMapperTest(unittest.TestCase):
    def setUp(self):
        self.connection = connect(URL_DATABASE)
        self.connection.execute("INSERT INTO BoardURL (url, idb) VALUES (\'URLTest\',\'9\')")
        self.idb = self.connection.execute("SELECT idb FROM BoardURL WHERE url=\'URLTest\'").fetchone()[0]
        self.connection.commit()

    def test_retrieve_idb(self):
        mapper = BoardURLDataMapper()
        self.assertEqual("9", mapper.retrieve_idb("URLTest"))

    def tearDown(self):
        self.connection.execute('DELETE FROM BoardURL')
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
