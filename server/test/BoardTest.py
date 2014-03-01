import unittest
from server.KanbanModel.Board import Board
from server.KanbanModel.Column import Column
from server.KanbanModel.Task import Task


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
