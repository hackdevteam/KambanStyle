import unittest


class Column():
  def __init__(self, title):
    self.__title = title

  def get_title(self):
    return self.__title


class ColumnTest(unittest.TestCase):
  def test_create_column(self):
    column=Column("MyTitle")
    self.assertEqual("MyTitle", column.get_title())
