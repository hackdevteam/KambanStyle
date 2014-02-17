class UserMapper:

	def __init__(self, user_store):
		self.user_store = user_store

	def user_list(self):
		return self.user_store.users()

	def insert(self, user):
		self.user_store.add(user)

	def delete(self, user_name):
		self.user_store.delete(user_name)

	def get_user(self, user_name):
		for user in self.user_store.users():
			if user_name == user.user_name:
				return user


