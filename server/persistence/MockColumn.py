import uuid


class MockColumn():
	def __init__(self, name):
		self.name = name
		self.id = uuid.uuid4()