responses = {}

poll_active = True

while poll_active:
	confirm = input("Would you like to take a vacation poll? (yes/no)  ")
	confirm.lower()
	
	if confirm == 'yes':
		name = input("\nWhat is your name? ")
		question = input("Where would your dream vacation be? ")
		
		responses[name] = question
		
		again = ("Would someone else like to take the poll again? (yes/no) ")
		
		if again == 'no':
			break
			
	else:
		print("\nThank you for your time!")
		poll_active = False

if responses != {}:
	print("\n--Poll Results--")
	for name, response in responses.items():
		print(name.title() + "'s dream vacation is in " + response.title() + 
			".")
