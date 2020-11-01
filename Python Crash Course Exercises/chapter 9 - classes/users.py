class Users():
	"""
	Creates a profile of an user
	Describes it
	Prints greeting to user
	"""
	
	def __init__(self, first, last, user_info=[]):
		"""Initialize name and other info"""
		self.first = first
		self.last = last
		self.user_info = user_info
		self.login_attempts = 0
		
	def describe_user(self):
		"""Prints summary of user"""
		if self.user_info:
			print(self.first.title() + " " + self.last.title() + ": ")
		else:
			print(self.first.title() + " " + self.last.title() + 
			": no info...")
			
		for i in self.user_info:
			print(" \t" + i)
		
	def greet_user(self):
		"""Greets the user"""
		print("Hi " + self.first.title() + " " + self.last.title() +
			"!")
			 
	def increment_login(self):
		"""Increments the login attempts by one"""
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		"""Resets the login attempts"""
		self.login_attempts = 0
		
		
		



