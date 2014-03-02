import os
from server.persistence.filesystem.operative_system import *

BOARD_SUFFIX = ".brd"


class UserBoardsManager():
	def __init__(self, user_base_folder):
		self._user_base_folder = user_base_folder

	def get_boards_ids(self):
		for dir_name, directories, files in os.walk(self._user_base_folder):
			return directories

	def save_board(self, board):
		create_directory(os.path.join(self._user_base_folder, board.id))
		serialise_object(board, os.path.join(self._user_base_folder, board.id + BOARD_SUFFIX))

	def load_board(self, board_id):
		return deserialise_object(os.path.join(self._user_base_folder, board_id + BOARD_SUFFIX))