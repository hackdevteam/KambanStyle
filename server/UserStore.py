class UserStore:

	def __init__(self):
		pass

	def insert_user(self, user):
		self.user_list.add(user)

	def add(self, user):
		self.user_list.add(user)

	def users(self):
		return self.user_list

	def delete(self, user_name):
		for user in self.user_list:
			if user.user_name == user_name:
				self.user_list.remove(user)
				return