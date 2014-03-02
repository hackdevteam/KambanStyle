import os
import unittest
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
		boards_manager.save_board()
		self.assertEqual(2, len(boards_manager.get_boards_ids()))

	def test_load_board(self):
		self.assertTrue(False)