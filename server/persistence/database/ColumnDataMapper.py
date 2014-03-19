from server.persistence.database.DataMapper import DataMapper


class ColumnDataMapper(DataMapper):
    def insert(self, column):
        self.query = "INSERT INTO column (title, idb) VALUES(?,?)"
        self.abstract_insert(column.get_title(), column.get_board_id())

    def retrieve(self, column_title):
        self.query = "SELECT * FROM column WHERE title=?"
        return self.abstract_retrieve(column_title)
