import os
import unittest
from server.kamban.model.Board import Board

from server.persistence.filesystem.UserBoardsManager import UserBoardsManager
from server.test.persistence.commons import remove_data, serialize_object

BASE_FOLDER = os.path.abspath("../resources")

DEMO_USER_NAME = "demo user"


class UsersBoardLoaderTest(unittest.TestCase):
	def setUp(self):
		remove_data(BASE_FOLDER)
		self.boards_manager = UserBoardsManager(os.path.join(BASE_FOLDER, DEMO_USER_NAME))

	def tearDown(self):
		remove_data(BASE_FOLDER)

	def test_getting_all_the_user_boards_ids(self):
		os.makedirs(os.path.join(BASE_FOLDER, DEMO_USER_NAME, "board 1"))
		os.makedirs(os.path.join(BASE_FOLDER, DEMO_USER_NAME, "board 2"))
		self.assertEqual(2, len(self.boards_manager.get_boards_ids()))

	def test_save_board(self):
		mock_board_1 = Board("Mock Board 1")
		mock_board_2 = Board("Mock Board 2")
		self.boards_manager.save_board(mock_board_1)
		self.boards_manager.save_board(mock_board_2)
		self.assertEqual(2, len(self.boards_manager.get_boards_ids()))
		self.assertTrue(mock_board_2.get_id() in self.boards_manager.get_boards_ids())
		self.assertTrue(mock_board_1.get_id() in self.boards_manager.get_boards_ids())

	def test_save_boards_with_the_same_name(self):
		self.boards_manager.save_board(Board("Board 1"))
		self.boards_manager.save_board(Board("Board 1"))
		self.boards_manager.save_board(Board("Board 1"))
		self.assertEqual(3, len(self.boards_manager.get_boards_ids()))

	def test_load_board(self):
		board = Board("Mock Board")
		serialize_object(os.path.join(BASE_FOLDER, DEMO_USER_NAME), board.get_id() + ".brd", board)
		loaded_board = self.boards_manager.load_board(self.boards_manager.get_boards_ids()[0])
		self.assertEqual("Mock Board", loaded_board.get_title())