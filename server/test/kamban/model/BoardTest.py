import unittest
from server.kanban.model.Board import Board


class BordTest(unittest.TestCase):
    def test_create_board(self):
        board = Board("MyBoardName")
        self.assertEqual("MyBoardName", board.get_title())
        self.assertIsNotNone(board.get_id())