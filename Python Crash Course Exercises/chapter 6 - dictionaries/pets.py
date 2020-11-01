caca = {
	'species': 'cat',
	'owner': 'alex',
	}
	
bruno = {
	'species': 'dog',
	'owner': 'gabriel',
	}

pets = [bruno, caca]

pet_name = ['bruno', 'caca']

digits = 0

for pet in pets:
	if pet == bruno:
		print("Pet: " + pet_name[digits].title())
		print("\tSpecies: " + pet['species'].title() + 
		"\n\tOwner: " + pet['owner'].title())
	else:
		print("Pet: " + pet_name[1].title())
		print("\tSpecies: " + pet['species'].title() + 
		"\n\tOwner: " + pet['owner'].title())

		
		


