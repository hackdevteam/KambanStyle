import uuid


class Column():
	def __init__(self, title):
		self.__title = title
		self.__id = str(uuid.uuid4())

	def get_title(self):
		return self.__title

	def get_id(self):
		return self.__id