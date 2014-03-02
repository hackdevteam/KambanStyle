from server.persistence.filesystem.operating_system import *
BOARD_SUFFIX = ".brd"


class UserBoardsManager():
	def __init__(self, user_base_folder):
		self._user_base_folder = user_base_folder

	def get_boards_ids(self):
		return list_directories(self._user_base_folder)

	def save_board(self, board):
		create_directory(join_paths(self._user_base_folder, board.id))
		serialise_object(board, join_paths(self._user_base_folder, board.id + BOARD_SUFFIX))

	def load_board(self, board_id):
		return deserialise_object(join_paths(self._user_base_folder, board_id + BOARD_SUFFIX))