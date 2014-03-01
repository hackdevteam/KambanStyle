import unittest
from server.KanbanModel.Column import Column
from server.KanbanModel.Task import Task


class Board():
  def __init__(self, name):
    self.__name = name
    self.__column_dictionary = {}

  def get_name(self):
    return self.__name

  def get_column(self, column_title):
    return self.__column_dictionary[column_title]

  def addColumn(self, column):
    self.__column_dictionary[column.get_title()] = column

  def add_task_to_column(self, column_title, task):
    self.__column_dictionary[column_title].add(task)

  def get_tasks_from_column(self, colunm_title):
    return self.__column_dictionary[colunm_title].get_tasks()

  def remove_task_from_column(self, column_title, task_title):
    self.__column_dictionary[column_title].remove(task_title)


class MyTestCase(unittest.TestCase):
  def test_create_board(self):
    board = Board("MyBoardName")
    self.assertEqual("MyBoardName", board.get_name())

  def test_add_column(self):
    board = Board("MyBoardName")
    board.addColumn(Column("MyTitle Column"))
    self.assertEqual("MyTitle Column", board.get_column("MyTitle Column").get_title())

  def test_add_task_to_column(self):
    board = Board("MyBoardName")
    board.addColumn(Column("MyTitle Column"))
    board.add_task_to_column("MyTitle Column", Task("MyTitle Task", "My Task Description"))
    self.assertEqual(1, len(board.get_tasks_from_column("MyTitle Column")))

  def test_remove_task_from_column(self):
    board = Board("MyBoardName")
    board.addColumn(Column("MyTitle Column"))
    board.add_task_to_column("MyTitle Column", Task("MyTitle Task", "My Task Description"))
    board.remove_task_from_column("MyTitle Column", "MyTitle Task")
    self.assertEqual(0, len(board.get_tasks_from_column("MyTitle Column")))
