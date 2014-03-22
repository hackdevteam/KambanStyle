import unittest
from server.kamban.model.Board import Board


class BoardTest(unittest.TestCase):
    def test_create_board(self):
        board = Board("MyBoardName")
        self.assertEqual("MyBoardName", board.get_title())
        self.assertIsNotNone(board.get_id())