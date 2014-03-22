from server.persistency.database.DataMapper import DataMapper


class ColumnDataMapper(DataMapper):
  def __init__(self):
    super().__init__()

  def insert(self, column):
    super.query = "INSERT INTO column (title, idb) VALUES(?,?,?)"
    super().abstract_insert((column.get_title(), column.get_board_id()))

