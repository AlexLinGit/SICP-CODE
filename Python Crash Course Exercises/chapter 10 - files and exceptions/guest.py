filename = 'guest_list.txt'

while True:
	name = input("What is your name?  ")
	
	if name == 'stop':
		break
	else:
		with open(filename, 'a') as guest_book:
			guest_book.write(name + " \n")
		
		print("Hi " + name.title())
