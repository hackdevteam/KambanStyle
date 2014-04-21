from server.kamban.model.Column import Column
from server.persistence.database.DataMapper import DataMapper


class ColumnDataMapper(DataMapper):
    def __init__(self):
        DataMapper()

    def insert(self, column):
        self.query = "INSERT INTO column (title, idb) VALUES(?,?)"
        return self.abstract_insert([column.get_title(), column.get_board_id()])

    def retrieve(self, idc):
        self.query = "SELECT * FROM column WHERE idc=?"
        column_tuple = self.abstract_retrieve([idc, ]).fetchone()
        return Column(column_tuple[1], column_tuple[2])

    def update(self, title, idb, idc):
        self.query = "UPDATE column SET title=?, idb=? WHERE idc=?"
        self.abstract_update([title, idb, idc])

