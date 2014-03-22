class PersistenceManager():
    def __init__(self, persistence):
        self.__persistence = persistence

    def get_boards_ids(self):
        return self.__persistence.get_boards_ids()

    def save_board(self, board):
        return self.__persistence.save_board(board)

    def load_board(self, board_id):
        return self.__persistence.load_board(board_id)

    def load_column(self, column_id, board_id):
        return self.__persistence.load_column(column_id, board_id)

    def get_columns_ids(self, board_id):
        return self.__persistence.get_columns_ids(board_id)

    def save_column(self, column):
        return self.__persistence.save_column(column)

    def save_task(self, task):
        return self.__persistence.save_task(task)

    def get_tasks_ids(self, column_id):
        return self.__persistence.get_tasks_ids(column_id)

    def delete_task(self, task_id):
        return self.__persistence.delete_task(task_id)