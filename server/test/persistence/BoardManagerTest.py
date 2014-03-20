import os
import unittest
from server.kamban.model.Board import Board
from server.kamban.model.Column import Column
from server.kamban.model.Task import Task

from server.persistence.filesystem.BoardManager import BoardManager
from server.test.persistence.commons import remove_data, serialize_object

BASE_FOLDER = os.path.abspath("../../resources")
TEST_BOARD_ID = "test_board"


class BoardManagerTest(unittest.TestCase):
    def setUp(self):
        remove_data(BASE_FOLDER)
        self.board_manager = BoardManager(BASE_FOLDER)

    def tearDown(self):
        remove_data(BASE_FOLDER)

    def test_getting_all_the_user_boards_ids(self):
        os.makedirs(os.path.join(BASE_FOLDER, "board 1"))
        os.makedirs(os.path.join(BASE_FOLDER, "board 2"))
        self.assertEqual(2, len(self.board_manager.get_boards_ids()))

    def test_save_boards_with_the_same_name(self):
        self.board_manager.save_board(Board("Board 1"))
        self.board_manager.save_board(Board("Board 1"))
        self.board_manager.save_board(Board("Board 1"))
        self.assertEqual(3, len(self.board_manager.get_boards_ids()))

    def test_load_board(self):
        board = Board("Mock Board")
        serialize_object(os.path.join(BASE_FOLDER), board.get_id() + ".brd", board)
        loaded_board = self.board_manager.load_board(self.board_manager.get_boards_ids()[0])
        self.assertEqual("Mock Board", loaded_board.get_title())

    def test_save_board(self):
        board_1 = Board("Mock Board 1")
        board_2 = Board("Mock Board 2")
        self.board_manager.save_board(board_1)
        self.board_manager.save_board(board_2)
        self.assertEqual(2, len(self.board_manager.get_boards_ids()))
        self.assertTrue(board_2.get_id() in self.board_manager.get_boards_ids())
        self.assertTrue(board_1.get_id() in self.board_manager.get_boards_ids())

    def test_load_column(self):
        column = Column("column inserted manually", TEST_BOARD_ID)
        serialize_object(os.path.join(BASE_FOLDER, TEST_BOARD_ID), column.get_id() + ".clm", column)
        loaded_column = self.board_manager.load_column(self.board_manager.get_columns_ids(TEST_BOARD_ID)[0], TEST_BOARD_ID)
        self.assertEqual("column inserted manually", loaded_column.get_title())

    def test_save_column(self):
        column_1 = Column("column 1", TEST_BOARD_ID)
        column_2 = Column("column 2", TEST_BOARD_ID)
        column_3 = Column("column 3", TEST_BOARD_ID)
        self.board_manager.save_column(column_1)
        self.board_manager.save_column(column_2)
        self.board_manager.save_column(column_3)
        self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_1.get_id()))))
        self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_2.get_id()))))
        self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_3.get_id()))))

    def test_get_columns_ids(self):
        self.board_manager.save_column(Column("column 1", TEST_BOARD_ID))
        self.board_manager.save_column(Column("column 2", TEST_BOARD_ID))
        self.board_manager.save_column(Column("column 3", TEST_BOARD_ID))
        self.assertEqual(3, len(self.board_manager.get_columns_ids(TEST_BOARD_ID)))

    def test_save_a_column_with_duplicated_name(self):
        self.board_manager.save_column(Column("column 1", TEST_BOARD_ID))
        self.board_manager.save_column(Column("column 1", TEST_BOARD_ID))
        self.assertEqual(2, len(self.board_manager.get_columns_ids(TEST_BOARD_ID)))

    def test_get_tasks_ids(self):
        column = Column("column 1", TEST_BOARD_ID)
        os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.get_id())))
        self.board_manager.save_task(Task("task 1", "", column.get_id()))
        self.board_manager.save_task(Task("task 1", "", column.get_id()))
        self.board_manager.save_task(Task("task 1", "", column.get_id()))
        self.assertEqual(3, len(self.board_manager.get_tasks_ids(column.get_id())))

    def test_save_a_task(self):
        column = Column("column 1", TEST_BOARD_ID)
        task = Task("title task 1", "description", column.get_id())
        self.board_manager.save_column(column)
        self.board_manager.save_task(task)
        self.assertEqual(task.get_id(), self.board_manager.get_tasks_ids(column.get_id())[0])

    def test_delete_a_task(self):
        column = Column("column 1", TEST_BOARD_ID)
        os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.get_id())))
        task_1 = Task("task 1", "", column.get_id())
        self.board_manager.save_task(task_1)
        self.board_manager.save_task(Task("task 2", "", column.get_id()))
        self.board_manager.save_task(Task("task 3", "", column.get_id()))
        self.assertEqual(3, len(self.board_manager.get_tasks_ids(column.get_id())))
        self.board_manager.delete_task(task_1.get_id())
        self.assertEqual(2, len(self.board_manager.get_tasks_ids(column.get_id())))

    def test_delete_an_non_existent_task(self):
        column = Column("column 1", TEST_BOARD_ID)
        os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, column.get_id()))
        task_1 = Task("task 1", "", column.get_id())
        self.board_manager.save_task(task_1)
        self.board_manager.save_task(Task("task 2", "", column.get_id()))
        self.assertEqual(2, len(self.board_manager.get_tasks_ids(column.get_id())))
        self.board_manager.delete_task(task_1.get_id())
        self.board_manager.delete_task(task_1.get_id())
        self.assertEqual(1, len(self.board_manager.get_tasks_ids(column.get_id())))