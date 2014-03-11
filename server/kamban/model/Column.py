import uuid


class Column():
    def __init__(self, title, board_id):
        self.__title = title
        self.__id = str(uuid.uuid4())
        self.__board_id = board_id

    def get_title(self):
        return self.__title

    def get_id(self):
        return self.__id

    def get_board_id(self):
        return self.__board_id