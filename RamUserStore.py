class RamUserStore:
	def __init__(self):
		self.user_list = set()

	def insert_user(self, user):
		self.user_list.add(user)

	def add(self, user):
		self.user_list.add(user)

	def users(self):
		return self.user_list