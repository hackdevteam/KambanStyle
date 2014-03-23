from server.kamban.model.Board import Board
import json


class BoardApiEndPoint(object):
    exposed = True

    def __init__(self, persistence):
        self.__persistence = persistence

    def POST(self, title):
        board = Board(title)
        self.__persistence.save_board(board)
        return json.dumps({"title": board.get_title(), "board_id": board.get_id()})