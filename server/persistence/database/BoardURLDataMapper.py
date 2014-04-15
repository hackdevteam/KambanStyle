from server.persistence.database.DataMapper import DataMapper

__author__ = 'Maca'


class BoardURLDataMapper(DataMapper):
    def __init__(self):
        DataMapper()

    def insert(self, url, id_board):
        self.query = "INSERT INTO BoardURL (url, idb) VALUES(?,?)"
        return self.abstract_insert([url, id_board])

    def retrieve_idb(self, url):
        self.query = "SELECT idb FROM BoardURL WHERE url=?"
        return self.abstract_retrieve([url, ]).fetchone()[0]