response = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	question = input("Who is your best friend? ")
	
	response[name] = question
	
	again = input("Would someone else like to take the poll? (yes/no):   ")
	if again == 'no':
			polling_active = False

print("\n--Poll Results--")
for name, fav in response.items():
	print(name.title() + "'s best friend is " + fav.title() + ".")
