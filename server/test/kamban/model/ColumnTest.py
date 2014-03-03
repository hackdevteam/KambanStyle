import unittest

from server.kamban.model.Column import Column


class ColumnTest(unittest.TestCase):
	def test_create_column(self):
		column = Column("MyTitle")
		self.assertEqual("MyTitle", column.get_title())
		self.assertIsNotNone(column.get_id())