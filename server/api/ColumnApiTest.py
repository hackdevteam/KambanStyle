import json
from server.KanbanModel.Column import Column


class ColumnApiEndPoint(object):

    def __init__(self, persistence):
        self.__persistance = persistence

    def POST(self, title):
        column = Column(title)
        self.__persistance.save()
        return json.dumps({"name": column.get_title(), "id": column.get_id})