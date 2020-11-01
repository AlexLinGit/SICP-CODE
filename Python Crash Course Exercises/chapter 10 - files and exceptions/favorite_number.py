import json

filename = 'fav_num.json'

def print_num():
	"""Prints and retrieves fav number"""
	try:
		with open(filename) as f_ob:
			num = json.load(f_ob)
			print("Your favorite number is " + str(num))
	except FileNotFoundError:
		new_fav_num()
		
def new_fav_num():
	"""Creates and stores new favorite number"""
	new_num = input("What is your favorite number?  ")
	with open(filename, 'w') as f_ob:
		json.dump(new_num, f_ob)
		

print_num()


