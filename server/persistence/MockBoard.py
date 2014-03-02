import uuid


class MockBoard():
	def __init__(self, board_name):
		self.name = board_name
		self.id = str(uuid.uuid4())