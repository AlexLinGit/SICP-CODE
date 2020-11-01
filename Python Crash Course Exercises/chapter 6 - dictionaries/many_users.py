users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'alin': {
		'first': 'alex',
		'last': 'lin',
		'location': 'earth',
		},
	}
	
for username, user_info in users.items():
	print("\nUnsername: " + username)
	
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
