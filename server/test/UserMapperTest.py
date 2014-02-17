import unittest
from server.RamUserStore import RamUserStore
from server.User import User
from server.UserMapper import UserMapper


class UserMapperTest(unittest.TestCase):
	def test_insert_user(self):
		user_mapper = UserMapper(RamUserStore())
		user_mapper.insert(User("ramclen", "1234"))
		user = user_mapper.get_user("ramclen")
		self.assertEqual(1, len(user_mapper.user_list()))
		self.assertEqual("ramclen", user.user_name)
		self.assertEqual("1234", user.password)

	def test_insert_duplicated_user(self):
		self.assertTrue(False)

	def test_delete_user(self):
		self.assertTrue(False)

	def test_delete_unexistent_user(self):
		self.assertTrue(False)

	