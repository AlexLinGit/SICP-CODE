prompt = "\nType a pizza topping (type 'quit' to exit): "

flag = True

while flag:
	message = input(prompt)
	
	if message == 'quit':
		flag = False
		continue 
	
	print("We'll add " + message + " to your pizza.")
	
