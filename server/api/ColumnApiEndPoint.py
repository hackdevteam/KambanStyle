import json

from server.kamban.model.Column import Column


class ColumnApiEndPoint(object):
    exposed = True

    def __init__(self, persistence):
        self.__persistance = persistence

    def POST(self, title, board_id):
        column = Column(title, board_id)
        self.__persistance.save_column(column)
        return json.dumps({"name": column.get_title(), "column_id": column.get_id(), "board_id": column.get_board_id()})