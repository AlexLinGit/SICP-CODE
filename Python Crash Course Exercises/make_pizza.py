def make_pizza(size, *toppings):
	"""Stores the toppings of a pizza"""
	print("\nMaking a " + str(size) + "-inch pizza with: ")
	for topping in toppings:
		print("- " + topping)
		
