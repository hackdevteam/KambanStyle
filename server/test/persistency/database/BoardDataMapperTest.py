import unittest
from server.kamban.model.Board import Board
from server.persistency.database.BoardDataMapper import BoardDataMapper


class BoardDataMapperTest(unittest.TestCase):
    def test_insert(self):
        mapper = BoardDataMapper()
        mapper.insert(Board("My Board"))
        self.assertEqual(2, len(mapper.retrive("My Board")))


if __name__ == '__main__':
    unittest.main()
