import unittest
from server.kamban.model.Board import Board
from server.persistence.database.BoardDataMapper import BoardDataMapper
from sqlite3 import connect

URL_DATABASE = "C:\\Users\Josue\Desktop\KanbanStyle.sqlite"


class BoardDataMapperTest(unittest.TestCase):
    def setUp(self):
        self.connection = connect(URL_DATABASE)
        self.connection.execute("INSERT INTO board (title) VALUES (\'FirstBoard\')")
        self.idb = self.connection.execute("SELECT idb FROM board WHERE title=\'FirstBoard\'").fetchone()[0]
        self.connection.commit()

    def test_insert(self):
        mapper = BoardDataMapper()
        board = Board("My Board")
        mapper.insert(board)
        self.assertEqual(board.get_title(), mapper.retrieve("My Board").get_title())

    def test_retrieve(self):
        mapper = BoardDataMapper()
        self.assertEqual("FirstBoard", mapper.retrieve("FirstBoard").get_title())

    def test_update(self):
        mapper = BoardDataMapper()
        mapper.update_title('FirstBoardModified', self.idb)
        self.assertEqual('FirstBoardModified', mapper.retrieve('FirstBoardModified').fetchone()[1])

    def tearDown(self):
        self.connection.execute('DELETE FROM board')
        self.connection.commit()
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
