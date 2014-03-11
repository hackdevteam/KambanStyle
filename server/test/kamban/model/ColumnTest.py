import unittest
from uuid import uuid4

from server.kamban.model.Column import Column


class ColumnTest(unittest.TestCase):
    def test_create_column(self):
        column = Column("MyTitle", str(uuid4()))
        self.assertEqual("MyTitle", column.get_title())
        self.assertIsNotNone(column.get_id())