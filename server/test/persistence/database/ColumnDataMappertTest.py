import unittest
from server.kanban.model.Column import Column
from server.persistence.database.ColumnDataMapper import ColumnDataMapper


class ColumnDataMapperTest(unittest.TestCase):

  def test_insert(self):
    mapper = ColumnDataMapper()
    mapper.insert(Column("My Column", 2))
    self.assertEqual(1, mapper.retrieve("My Column").fetchall().__sizeof__())

  def test_retrieve(self):
      mapper = ColumnDataMapper()
      self.assertEqual("", mapper.retrieve("FirstColumn").fetchone()[1])


if __name__ == '__main__':
  unittest.main()