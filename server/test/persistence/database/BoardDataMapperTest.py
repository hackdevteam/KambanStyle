import unittest
from server.kanban.model.Board import Board
from server.persistence.database.BoardDataMapper import BoardDataMapper


class BoardDataMapperTest(unittest.TestCase):

  def test_insert(self):
    mapper = BoardDataMapper()
    mapper.insert(Board("My Board"))
    self.assertEqual("My Board", mapper.retrieve("My Board").fetchone()[1])

  def test_retrive(self):
      mapper = BoardDataMapper()
      self.assertEqual("FirstBoard", mapper.retrieve("FirstBoard").fetchone()[1])


if __name__ == '__main__':
  unittest.main()
