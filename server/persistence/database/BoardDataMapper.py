from server.kamban.model.Board import Board
from server.persistence.database.DataMapper import DataMapper


class BoardDataMapper(DataMapper):
    def __init__(self):
        DataMapper()

    def insert(self, board):
        self.query = "INSERT INTO board (title) VALUES(?)"
        return self.abstract_insert([board.get_title(), ])

    def retrieve(self, idb):
        self.query = "SELECT * FROM board WHERE idb=?"
        board_tuple = self.abstract_retrieve([idb, ]).fetchone()
        return Board(board_tuple[1])

    def update(self, title, idb):
        self.query = "UPDATE board SET title=? WHERE idb=?"
        self.abstract_update([title, idb])

