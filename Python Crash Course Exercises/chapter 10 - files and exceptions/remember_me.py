import json

filename = 'usernames.json'

def greet_user():
	"""Greets user by name"""
	user = get_stored_username()
	user = user.split()
	
	if user:
		for name in user:
			print("\t" + name)
		confirm = input("Is your name on the list? (yes/no)   ")
		if confirm == 'yes':
			verify = input("What is your username?  \n")
			if verify in user:
				print("Hi " + verify)
		elif confirm == 'no':
			append_user()
		else:
			print("Please answer yes or no")
	else:
		get_new_username()

def get_new_username():
	"""Creates new username"""
	username = input("What is your name?   ")
	with open(filename, 'w') as f_ob:
		json.dump(username, f_ob)
		print("Your username is now stored")
	
def get_stored_username():
	"""Returns a stored username if one"""
	try:
		with open(filename) as f_ob:
			name = json.load(f_ob)
	except FileNotFoundError:
		return None
	else:
		return name

def append_user():
	"""Adds a new user to the file"""
	username = input("What is your name?   ")
	with open(filename) as f_ob:
		names = json.load(f_ob)
		names += ' ' + username
	
	with open(filename, 'w') as f_ob:
		json.dump(names, f_ob)
		print("Your username is now stored")



greet_user()
