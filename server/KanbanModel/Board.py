import uuid


class Board():

    def __init__(self, name):
        self._name = name
        self._id = str(uuid.uuid4())

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id
