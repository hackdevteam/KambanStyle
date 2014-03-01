import unittest
from server.KanbanModel.Column import Column


class Board(object):

  def __init__(self, name):
    self.__name = name
    self.__column_dictionary = {}

  def get_name(self):
    return self.__name

  def get_column(self, column_title):
    return self.__column_dictionary[column_title]

  def addColumn(self, column):
    self.__column_dictionary[column.get_title()] = column


class MyTestCase(unittest.TestCase):
  def test_create_board(self):
    board = Board("MyBoardName")
    self.assertEqual("MyBoardName", board.get_name())

  def test_add_column(self):
    board = Board("MyBoardName")
    board.addColumn(Column("MyTitle Column"))
    self.assertEqual("MyTitle Column", board.get_column("MyTitle Column").get_title())
