import os


class UserBoardsManager():
	def __init__(self, user_base_folder):
		self._user_base_folder = user_base_folder

	def get_boards_ids(self):
		for dir_name, directories, files in os.walk(self._user_base_folder):
			return directories