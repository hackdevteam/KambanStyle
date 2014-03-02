import os
import unittest
from server.persistence.MockBoard import MockBoard

from server.persistence.filesystem.UserBoardsManager import UserBoardsManager
from server.test.persistence.commons import remove_data, BASE_FOLDER, serialize_object


DEMO_USER_NAME = "demo user"


class UsersBoardLoaderTest(unittest.TestCase):
	def setUp(self):
		remove_data(os.path.join(BASE_FOLDER, DEMO_USER_NAME))
		self.boards_manager = UserBoardsManager(os.path.join(BASE_FOLDER, DEMO_USER_NAME))

	def tearDown(self):
		remove_data(os.path.join(BASE_FOLDER, DEMO_USER_NAME))

	def test_getting_all_the_user_boards_ids(self):
		os.makedirs(os.path.join(BASE_FOLDER, DEMO_USER_NAME, "board 1"))
		os.makedirs(os.path.join(BASE_FOLDER, DEMO_USER_NAME, "board 2"))
		self.assertEqual(2, len(self.boards_manager.get_boards_ids()))

	def test_save_board(self):
		mock_board_1 = MockBoard("Mock Board 1")
		mock_board_2 = MockBoard("Mock Board 2")
		self.boards_manager.save_board(mock_board_1)
		self.boards_manager.save_board(mock_board_2)
		self.assertEqual(2, len(self.boards_manager.get_boards_ids()))
		self.assertTrue(mock_board_2.id in self.boards_manager.get_boards_ids())
		self.assertTrue(mock_board_1.id in self.boards_manager.get_boards_ids())

	def test_save_boards_with_the_same_name(self):
		self.boards_manager.save_board(MockBoard("Board 1"))
		self.boards_manager.save_board(MockBoard("Board 1"))
		self.boards_manager.save_board(MockBoard("Board 1"))
		self.assertEqual(3, len(self.boards_manager.get_boards_ids()))

	def test_load_board(self):
		board = MockBoard("Mock Board")
		serialize_object(os.path.join(BASE_FOLDER, DEMO_USER_NAME), board.id + ".brd", board)
		loaded_board = self.boards_manager.load_board(self.boards_manager.get_boards_ids()[0])
		self.assertEqual("Mock Board", loaded_board.name)