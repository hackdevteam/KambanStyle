from server.persistence.database.DataMapper import DataMapper


class BoardDataMapper(DataMapper):
  def __init__(self):
    super.__init__()

  def insert(self, board):
    self.query = "INSERT INTO my_board (title) VALUES(?)"
    self.abstract_insert(board.get_title())

  def retrive(self, board_title):
    self.query = "SELECT * FROM my_board WHERE title=\" ? \""
    self.abstract_retrive(board_title)