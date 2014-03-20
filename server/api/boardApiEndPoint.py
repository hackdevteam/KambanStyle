from server.kamban.model.Board import Board
import json


class BoardApiEndPoint(object):
    exposed = True

    def __init__(self, persistence):
        self.__persistence = persistence

    def POST(self, name):
        board = Board(name)
        self.__persistence.save_board(board)
        return json.dumps({"name": board.get_title(), "id": board.get_id()})