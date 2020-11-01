import json

filename = 'usernames.json'
with open(filename) as f_ob:
	names = json.load(f_ob)
	print("Hi " + names.title())
