from server.persistence.database.DataMapper import DataMapper


class BoardDataMapper(DataMapper):
    def __init__(self):
        DataMapper()

    def insert(self, board):
        self.query = "INSERT INTO board (title) VALUES(?)"
        self.abstract_insert(board.get_title())

    def retrieve(self, board_title):
        self.query = "SELECT * FROM board WHERE title=?"
        return self.abstract_retrieve(board_title)