import uuid


class Task():
	def __init__(self, title, description, column_id):
		self.__title = title
		self.__id = str(uuid.uuid4())
		self.__column_id = column_id
		self.__description = description

	def get_title(self):
		return self.__title

	def get_description(self):
		return self.__description

	def get_column_id(self):
		return self.__column_id

	def get_id(self):
		return self.__id