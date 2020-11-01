prompt = "How old are you?  "

while True:
	message = input(prompt)
	
	if str(message) == 'quit':
		break
	
	if int(message) < 3:
		print("Free")
	elif int(message) < 12:
		print("$10")
	elif int(message) >= 12:
		print("$15")
	else:
		continue
	
