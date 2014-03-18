import os
import unittest
from server.kamban.model.Column import Column
from server.kamban.model.Task import Task

from server.persistence.filesystem.BoardManager import BoardManager
from server.test.persistence.filesystem.commons import remove_data, serialize_object

BASE_FOLDER = os.path.abspath("../../resources")
TEST_BOARD_ID = "test_board"


class BoardManagerTest(unittest.TestCase):
    def setUp(self):
        remove_data(BASE_FOLDER)
        self.board_manager = BoardManager(TEST_BOARD_ID, BASE_FOLDER)

    def tearDown(self):
        remove_data(BASE_FOLDER)

    def test_load_column(self):
        column = Column("column inserted manually")
        serialize_object(os.path.join(BASE_FOLDER, TEST_BOARD_ID), column.get_id() + ".clm", column)
        loaded_column = self.board_manager.load_column(self.board_manager.get_columns_ids()[0])
        self.assertEqual("column inserted manually", loaded_column.get_title())

    def test_save_column(self):
        column_1 = Column("column 1")
        column_2 = Column("column 2")
        column_3 = Column("column 3")
        self.board_manager.save_column(column_1)
        self.board_manager.save_column(column_2)
        self.board_manager.save_column(column_3)
        self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_1.get_id()))))
        self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_2.get_id()))))
        self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_3.get_id()))))

    def test_get_columns_ids(self):
        self.board_manager.save_column(Column("column 1"))
        self.board_manager.save_column(Column("column 2"))
        self.board_manager.save_column(Column("column 3"))
        self.assertEqual(3, len(self.board_manager.get_columns_ids()))

    def test_save_a_column_with_duplicated_name(self):
        self.board_manager.save_column(Column("column 1"))
        self.board_manager.save_column(Column("column 1"))
        self.assertEqual(2, len(self.board_manager.get_columns_ids()))

    def test_get_tasks_ids(self):
        column = Column("column 1")
        os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.get_id())))
        self.board_manager.save_task(Task("task 1", "", column.get_id()))
        self.board_manager.save_task(Task("task 1", "", column.get_id()))
        self.board_manager.save_task(Task("task 1", "", column.get_id()))
        self.assertEqual(3, len(self.board_manager.get_tasks_ids(column.get_id())))

    def test_save_a_task(self):
        column = Column("column 1")
        task = Task("title task 1", "description", column.get_id())
        self.board_manager.save_column(column)
        self.board_manager.save_task(task)
        self.assertEqual(task.get_id(), self.board_manager.get_tasks_ids(column.get_id())[0])

    def test_delete_a_task(self):
        column = Column("column 1")
        os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.get_id())))
        task_1 = Task("task 1", "", column.get_id())
        self.board_manager.save_task(task_1)
        self.board_manager.save_task(Task("task 2", "", column.get_id()))
        self.board_manager.save_task(Task("task 3", "", column.get_id()))
        self.assertEqual(3, len(self.board_manager.get_tasks_ids(column.get_id())))
        self.board_manager.delete_task(task_1.get_id())
        self.assertEqual(2, len(self.board_manager.get_tasks_ids(column.get_id())))

    def test_delete_an_non_existent_task(self):
        column = Column("column 1")
        os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.get_id())))
        task_1 = Task("task 1", "", column.get_id())
        self.board_manager.save_task(task_1)
        self.board_manager.save_task(Task("task 2", "", column.get_id()))
        self.assertEqual(2, len(self.board_manager.get_tasks_ids(column.get_id())))
        self.board_manager.delete_task(task_1.get_id())
        self.board_manager.delete_task(task_1.get_id())
        self.assertEqual(1, len(self.board_manager.get_tasks_ids(column.get_id())))