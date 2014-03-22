from server.persistence.filesystem.operating_system import *

COLUMN_PROPERTIES_SUFFIX = ".clm"
BOARD_PROPERTIES_SUFFIX = ".brd"


class FilesystemPersistence():
    def __init__(self, database_url):
        self._working_directory = database_url.get_resource()

    def get_boards_ids(self):
        return list_directories(self._working_directory)

    def save_board(self, board):
        create_directory(join_paths(self._working_directory, board.get_id()))
        serialise_object(board, join_paths(self._working_directory, board.get_id() + BOARD_PROPERTIES_SUFFIX))

    def load_board(self, board_id):
        return deserialise_object(join_paths(self._working_directory, board_id + BOARD_PROPERTIES_SUFFIX))

    def get_columns_ids(self, board_id):
        return list_directories(join_paths(self._working_directory, board_id))

    def load_column(self, column_id, board_id):
        return deserialise_object(join_paths(self._working_directory, board_id, column_id + COLUMN_PROPERTIES_SUFFIX))

    def save_column(self, column):
        create_directory(join_paths(self._working_directory, column.get_board_id(), column.get_id()))
        serialise_object(column, join_paths(self._working_directory, column.get_board_id(), column.get_id() + COLUMN_PROPERTIES_SUFFIX))

    def get_tasks_ids(self, column_id):
        return list_files(join_paths(self._working_directory, find_parent_name(self._working_directory, column_id), column_id))

    def save_task(self, task):
        board_id = find_parent_name(self._working_directory, task.get_column_id())
        serialise_object(task, join_paths(self._working_directory, board_id, task.get_column_id(), task.get_id()))

    def delete_task(self, task_id):
        column_id = find_parent_name(self._working_directory, task_id)
        if column_id is None:
            return
        board_id = find_parent_name(self._working_directory, column_id)
        remove(join_paths(self._working_directory, board_id, column_id, task_id))