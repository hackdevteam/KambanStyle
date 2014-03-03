from server.KanbanModel.Board import Board
import json

class BoardApiEndPoint(object):
    exposed = True

    def __init__(self, persistence):
        self.__persistence = persistence

    def POST(self, name):
        board = Board(name)
        self.__persistence.save(board)
        return json.dumps({"name": board.get_name(), "id": board.get_id()})