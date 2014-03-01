class Column():
  def __init__(self, title):
    self.__title = title


class ColumnTest:
  def test_create_column(self):
    column=Column("MyTitle")
    self.assertEqual("MyTitle", column.get_title())
  