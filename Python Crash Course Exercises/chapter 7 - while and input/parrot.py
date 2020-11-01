prompt = "\nTell me something, and I'll repeat it."
prompt += "\nType 'quit' to end the program. "

flag = True

while flag:
	message = input(prompt)
	
	if message == 'quit':
		flag = False
	
	else:
		print(message)
	
