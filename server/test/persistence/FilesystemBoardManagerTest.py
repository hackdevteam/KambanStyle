import os
import pickle
import shutil
import unittest

from server.persistence.MockColumn import MockColumn
from server.persistence.MockTask import MockTask
from server.persistence.filesystem.BoardManager import BoardManager

TEST_BOARD_ID = "test_board"
BASE_FOLDER = os.path.abspath("../../resources")


class FilesystemBoardManagerTest(unittest.TestCase):

	def setUp(self):
		self.remove_data()
		self.board_manager = BoardManager(TEST_BOARD_ID, BASE_FOLDER)

	def tearDown(self):
		self.remove_data()

	def test_load_column(self):
		serialize_column(MockColumn("column inserted manually"))
		loaded_column = self.board_manager.load_column(self.board_manager.get_columns_ids()[0])
		self.assertEqual("column inserted manually", loaded_column.name)

	def test_save_column(self):
		column_1 = MockColumn("column 1")
		column_2 = MockColumn("column 2")
		column_3 = MockColumn("column 3")
		self.board_manager.save_column(column_1)
		self.board_manager.save_column(column_2)
		self.board_manager.save_column(column_3)
		self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_1.id))))
		self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_2.id))))
		self.assertTrue(os.path.exists(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column_3.id))))

	def test_delete_column(self):
		self.assertTrue(False)

	def test_get_columns_ids(self):
		column_1 = MockColumn("column 1")
		column_2 = MockColumn("column 2")
		column_3 = MockColumn("column 3")
		self.board_manager.save_column(column_1)
		self.board_manager.save_column(column_2)
		self.board_manager.save_column(column_3)
		self.assertEqual(3, len(self.board_manager.get_columns_ids()))

	def test_save_a_column_with_duplicated_name(self):
		self.board_manager.save_column(MockColumn("column 1"))
		self.board_manager.save_column(MockColumn("column 1"))
		self.assertEqual(2, len(self.board_manager.get_columns_ids()))

	def test_get_tasks_ids(self):
		column = MockColumn("column 1")
		os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.id)))
		task_1 = MockTask("task 1", "", column.id)
		task_2 = MockTask("task 1", "", column.id)
		task_3 = MockTask("task 1", "", column.id)
		self.board_manager.save_task(task_1)
		self.board_manager.save_task(task_2)
		self.board_manager.save_task(task_3)
		self.assertEqual(3, len(self.board_manager.get_tasks_ids(column.id)))

	def test_save_a_task(self):
		column = MockColumn("column 1")
		task = MockTask("title task 1", "description", column.id)
		self.board_manager.save_column(column)
		self.board_manager.save_task(task)
		self.assertEqual(task.id, self.board_manager.get_tasks_ids(column.id)[0])

	def test_delete_a_task(self):
		column = MockColumn("column 1")
		os.makedirs(os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.id)))
		task_1 = MockTask("task 1", "", column.id)
		task_2 = MockTask("task 2", "", column.id)
		task_3 = MockTask("task 3", "", column.id)
		self.board_manager.save_task(task_1)
		self.board_manager.save_task(task_2)
		self.board_manager.save_task(task_3)
		self.assertEqual(3, len(self.board_manager.get_tasks_ids(column.id)))
		self.board_manager.delete_task(task_1.id)
		self.assertEqual(2, len(self.board_manager.get_tasks_ids(column.id)))
		self.assertTrue(False)

	def test_delete_a_deleted_task(self):
		self.assertTrue(False)

	def remove_data(self):
		data_path = os.path.abspath(os.path.join(BASE_FOLDER, TEST_BOARD_ID))
		if os.path.exists(data_path):
			shutil.rmtree(data_path)


def serialize_column(column):
		working_directory = os.path.join(BASE_FOLDER, TEST_BOARD_ID, str(column.id))
		column_serialized_path = os.path.join(working_directory, ".clm")
		os.makedirs(working_directory)
		column_file = open(column_serialized_path, "w+")
		pickle.dump(column, column_file)
		column_file.close()
