import uuid


class MockTask():
	def __init__(self, tittle, description, column_id):
		self.tittle = tittle
		self.description = description
		self.column_id = column_id
		self.id = str(uuid.uuid4())