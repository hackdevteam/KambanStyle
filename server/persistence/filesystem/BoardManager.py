import os
from os.path import join
from server.persistence.filesystem.operative_system import *

COLUMN_PROPERTIES_SUFFIX = ".clm"


class BoardManager():
	def __init__(self, board_id, base_directory):
		self._board_id = board_id
		self._base_directory = base_directory
		self._working_directory = os.path.join(base_directory, board_id)

	def get_columns_ids(self):
		for dir_name, directories, files in os.walk(self._working_directory):
			return directories

	def load_column(self, column_id):
		column_properties_path = join(self._working_directory, column_id, COLUMN_PROPERTIES_SUFFIX)
		column = deserialize_object(column_properties_path)
		return column

	def save_column(self, column):
		column_directory = join(self._working_directory, column.id)
		column_properties_file = join(self._working_directory, column.id + COLUMN_PROPERTIES_SUFFIX)
		create_directory(column_directory)
		serialize_object(column, column_properties_file)

	def get_tasks_ids(self, column_id):
		tasks_ids = []
		for board, directories, tasks in os.walk(os.path.join(self._working_directory, column_id)):
			tasks_ids.extend(tasks)
		return tasks_ids

	def save_task(self, task):
		task_properties_file = join(self._working_directory, task.column_id, task.id)
		serialize_object(task, task_properties_file)

	def delete_task(self, task_id):
		for dir_name, directories, files in os.walk(self._working_directory):
			if task_id in files:
				os.remove(os.path.join(dir_name, task_id))