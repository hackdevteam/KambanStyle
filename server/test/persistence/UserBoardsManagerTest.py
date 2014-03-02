import os
import unittest
from server.persistence.filesystem.MockBoard import MockBoard
from server.persistence.filesystem.UserBoardsManager import UserBoardsManager
from server.test.persistence.commons import remove_data

DEMO_USER_NAME = "demo user"
BASE_FOLDER = os.path.abspath("../../resources")


class UsersBoardLoaderTest(unittest.TestCase):

	def setUp(self):
		remove_data(os.path.join(BASE_FOLDER, DEMO_USER_NAME))

	def tearDown(self):
		remove_data(os.path.join(BASE_FOLDER, DEMO_USER_NAME))

	def test_getting_all_the_user_boards_ids(self):
		os.makedirs(os.path.join(BASE_FOLDER, DEMO_USER_NAME, "board 1"))
		os.makedirs(os.path.join(BASE_FOLDER, DEMO_USER_NAME, "board 2"))
		boards_manager = UserBoardsManager(os.path.join(BASE_FOLDER, DEMO_USER_NAME))
		self.assertEqual(2, len(boards_manager.get_boards_ids()))

	def test_save_board(self):
		boards_manager = UserBoardsManager(os.path.join(BASE_FOLDER, DEMO_USER_NAME))
		mock_board_1 = MockBoard("Mock Board 1")
		mock_board_2 = MockBoard("Mock Board 2")
		boards_manager.save_board(mock_board_1)
		boards_manager.save_board(mock_board_2)
		self.assertEqual(2, len(boards_manager.get_boards_ids()))
		self.assertEqual(mock_board_1.id, boards_manager.get_boards_ids()[0])
		self.assertEqual(mock_board_2.id, boards_manager.get_boards_ids()[1])

	def test_load_board(self):
		self.assertTrue(False)