usernames = ['alexthegreat', 'admin', 'john123', 'bobs',
			'pokeman32']

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hello admin.  Would you like to see a special report?")
		else:
			print("Hello " + username.title() + "!")
else:
	print("We need some users!")
