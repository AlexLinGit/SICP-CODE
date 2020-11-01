prompt = "\nType the name of a city, any city."
prompt += "\n(Type 'quit' when you are done)    "

while True:
	message = input(prompt)
	
	if message == 'quit':
		break
	
	else:
		print(message)
