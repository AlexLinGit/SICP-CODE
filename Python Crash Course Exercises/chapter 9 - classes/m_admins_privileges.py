from users import Users


class Admins(Users):
	"""Represents the admins who have different type sof control"""
	
	def __init__(self, first, last, user_info):
		"""Initializes the admin attributes"""
		super().__init__(first, last, user_info)
		self.privileges = Privileges()


class Privileges():
	"""Gives admin rights and shows admin rights"""
	
	def __init__(self):
		"""Initializes privileges"""
		privileges = ['can edit, delete posts, ban users']
		self.privileges = privileges
	
	def show_privileges(self):
		"""Shows privileges of a user"""
		print("Privileges: ")
		for privilege in self.privileges:
			print("    -" + privilege)
