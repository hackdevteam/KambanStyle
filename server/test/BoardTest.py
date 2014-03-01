import unittest


class Board(object):

  def __init__(self, name):
    self.__name = name

  def get_name(self):
    return self.__name


class MyTestCase(unittest.TestCase):
  def test_create_board(self):
    board = Board("MyBoardName")
    self.assertEqual("MyBoardName", board.get_name())