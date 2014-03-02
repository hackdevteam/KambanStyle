import os
import unittest
from server.persistence.MockUser import MockUser
from server.persistence.filesystem.UserBoardsLoader import UserBoardsLoader


class UsersBoardLoaderTest(unittest.TestCase):

	def test_getting_all_the_user_boards_ids(self):
		logged_user = MockUser("demo user")
		os.makedirs(os.path.join(logged_user.user_name, "board 1"))
		os.makedirs(os.path.join(logged_user.user_name, "board 2"))
		boards_loader = UserBoardsLoader(logged_user)
		self.assertEqual(2, len(boards_loader.get_boards_ids()))

	def test_add_board(self):
		self.assertTrue(False)