from server.persistence.filesystem.operating_system import *

COLUMN_PROPERTIES_SUFFIX = ".clm"


class BoardManager():
	def __init__(self, board_id, base_directory):
		self._working_directory = join_paths(base_directory, board_id)

	def get_columns_ids(self):
		return list_directories(self._working_directory)

	def load_column(self, column_id):
		return deserialise_object(join_paths(self._working_directory, column_id + COLUMN_PROPERTIES_SUFFIX))

	def save_column(self, column):
		create_directory(join_paths(self._working_directory, column.id))
		serialise_object(column, join_paths(self._working_directory, column.id + COLUMN_PROPERTIES_SUFFIX))

	def get_tasks_ids(self, column_id):
		return list_files(join_paths(self._working_directory, column_id))

	def save_task(self, task):
		serialise_object(task, join_paths(self._working_directory, task.column_id, task.id))

	def delete_task(self, task_id):
		for column_directory in list_directories(self._working_directory):
			for task_file in list_files(join_paths(self._working_directory, column_directory)):
				if task_id in task_file:
					remove(join_paths(self._working_directory, column_directory, task_id))
					return