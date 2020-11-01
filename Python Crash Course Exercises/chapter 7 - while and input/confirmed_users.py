unconfirmed_users = ['alex', 'jerry', 'david',]
confirmed_users = []

while unconfirmed_users:
	current_users = unconfirmed_users.pop()
	print("Verifying: " + current_users.title()) 
	
	confirmed_users.append(current_users)
	
print("\nVerified users: ")
for user in confirmed_users:
	print(user.title())
