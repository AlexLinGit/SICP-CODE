def make_shirt(message='default message', shirt_size='default', ):
	"""Prints a custom shirt"""
	while True:
		if shirt_size == 'default':
			print("Enter a shirt size please")
		if message == 'default message':
			print("A plain shirt?")
		break
	
	if shirt_size != 'default' and message != 'default message':
		print("You ordered a " + shirt_size + " sized shirt with the message: " +
	      "\n\t" + message)
	elif shirt_size != 'default':
		print("You ordered a " + shirt_size)
	elif message != 'default message':
		print("You want the shirt to say: " + "\n\t" + message)
	   
make_shirt()
