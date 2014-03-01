import os
from server.persistence import loader
from server.persistence import saver

BASE_FOLDER = os.path.abspath("../../resources")


class BoardManager():
	def __init__(self, board_id):
		self.board_id = board_id
		self.working_directory = os.path.join(BASE_FOLDER, board_id)

	def columns_ids(self):
		return os.walk(self.working_directory).next()

	def load_column(self, column_id):
		return loader.load(self.working_directory, column_id)

	def save_column(self, column):
		saver.save_column(self.working_directory, column)