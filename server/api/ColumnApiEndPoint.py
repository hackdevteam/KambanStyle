import json

from server.kamban.model.Column import Column


class ColumnApiEndPoint(object):
    exposed = True

    def __init__(self, persistence):
        self.__persistance = persistence

    def POST(self, title):
        column = Column(title, str(uuid4()))
        self.__persistance.save(column)
        return json.dumps({"name": column.get_title(), "id": column.get_id(), "board_id": column.get_board_id()})