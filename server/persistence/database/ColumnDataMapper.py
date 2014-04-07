from server.persistence.database.DataMapper import DataMapper


class ColumnDataMapper(DataMapper):
    def __init__(self):
        DataMapper()

    def insert(self, column):
        self.query = "INSERT INTO column (title, idb) VALUES(?,?)"
        return self.abstract_insert([column.get_title(), column.get_board_id()])

    def retrieve(self, column_title):
        self.query = "SELECT * FROM column WHERE title=?"
        return self.abstract_retrieve([column_title, ])

    def update_title(self, title, idc):
        self.query = "UPDATE column SET title=? WHERE idc=?"
        self.abstract_update([title, idc])

    def update_idb(self, idb, idc):
        self.query = "UPDATE column SET idb=? WHERE idc=?"
        self.abstract_update([idb, idc])

