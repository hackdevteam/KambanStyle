import unittest
from server.kamban.model.Column import Column
from server.persistence.database.ColumnDataMapper import ColumnDataMapper


class ColumnDataMapperTest(unittest.TestCase):
    def test_insert(self):
        mapper = ColumnDataMapper()
        mapper.insert(Column("My Column", 2))
        self.assertEqual("My Column", mapper.retrieve("My Column").fetchone()[1])

    def test_retrieve(self):
        mapper = ColumnDataMapper()
        self.assertEqual("FirstColumn", mapper.retrieve("FirstColumn").fetchone()[1])


if __name__ == '__main__':
    unittest.main()
