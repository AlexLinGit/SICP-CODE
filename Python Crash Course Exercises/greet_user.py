def greet_users(names):
	"""Greets users in a list"""
	for name in names:
		msg = "Hi " + name.title() + "!"
		print(msg)
		

usernames = ['alex', 'noah', 'jon', 'angelo']		
greet_users(usernames)
