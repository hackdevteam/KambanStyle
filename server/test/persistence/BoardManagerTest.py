import os
import shutil
import unittest

from server.persistence.BoardManager import BoardManager
from server.persistence.MockColumn import MockColumn


TEST_BOARD_ID = "test_board"


class BoardManagerTest(unittest.TestCase):

	def setUp(self):
		self.remove_data()

	def tearDown(self):
		self.remove_data()

	def test_load_column(self):
		boar_manager = BoardManager(TEST_BOARD_ID)
		boar_manager.save_column(MockColumn("column 1"))
		boar_manager.save_column(MockColumn("column 2"))
		column = boar_manager.load_column(boar_manager.columns_ids()[0])
		self.assertEqual("column 1", column.name)

	def test_save_column(self):
		boar_manager = BoardManager(TEST_BOARD_ID)
		boar_manager.save_column(MockColumn("column 1"))
		boar_manager.save_column(MockColumn("column 2"))
		boar_manager.save_column(MockColumn("column 3"))
		self.assertEqual(3, len(boar_manager.columns_ids()))

	def test_save_a_column_with_duplicated_name(self):
		boar_manager = BoardManager(TEST_BOARD_ID)
		boar_manager.save_column(MockColumn("column 1"))
		boar_manager.save_column(MockColumn("column 1"))
		self.assertEqual(2, len(boar_manager.columns_ids()))

	def test_save_a_task(self):
		pass

	def test_save_several_tasks(self):
		pass

	def test_delete_a_task(self):
		pass

	def test_delete_a_deleted_task(self):
		pass
	
	def remove_data(self):
		data_path = os.path.abspath("../../resources/" + TEST_BOARD_ID)
		if os.path.exists(data_path):
			shutil.rmtree(data_path)
