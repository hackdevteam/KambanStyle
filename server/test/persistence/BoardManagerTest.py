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
		column = boar_manager.load_column("column 1")
		self.assertEqual("column 1", column.id)

	def test_save_column(self):
		boar_manager = BoardManager(TEST_BOARD_ID)
		boar_manager.save_column(MockColumn("column1"))
		boar_manager.save_column(MockColumn("column2"))
		boar_manager.save_column(MockColumn("column3"))
		self.assertEqual(3, len(boar_manager.columns_ids()))

	def remove_data(self):
		data_path = os.path.abspath("../../resources/" + TEST_BOARD_ID)
		if os.path.exists(data_path):
			shutil.rmtree(data_path)
