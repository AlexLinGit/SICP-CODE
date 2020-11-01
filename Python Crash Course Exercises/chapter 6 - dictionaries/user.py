user_0 = {
	'username': 'joe123',
	'first_name': 'joe',
	'last_name': 'badger',
	}
	
user_1= {
	'username': 'lin5nity',
	'first_name': 'alex',
	'last_name': 'lin',
	}
	
user_2 = {
	'username': 'ahkmedB',
	'first_name': 'ahman',
	'last_name': 'omari',
	}

users = [user_0, user_1, user_2,]

for user in users:
	print("\nUsername: " + user['username'].title())
	print("\tFirst name: " + user['first_name'].title() + 
	"\n\tLast name: " + user['last_name'].title())
