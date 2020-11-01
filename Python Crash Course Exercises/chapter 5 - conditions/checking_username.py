current_users = ['jones12', 'afdd21', 'alex', 'thesenuts', 'hiya']
new_users = ['jOnes12', 'Jopelin1', 'Alex', 'thesis', 'noya']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Pick a new username.")
	else:
		print("Hi " + new_user + "!")
			
