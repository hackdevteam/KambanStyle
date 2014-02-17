from server.UserStore import UserStore


class RamUserStore(UserStore):
	def __init__(self):
		self.user_list = set()