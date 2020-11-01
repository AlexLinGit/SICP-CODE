def print_models(unprinted_designs, completed_models):
	"""
	Simulates printing a design, until none are left
	Moves them to seperate list
	"""
	
	while unprinted_designs:
		design = unprinted_designs.pop()
		print("Currently printing: " + design)
		completed_models.append(design)
			

def show_models(completed_models):
	"""
	Shows a list of printed models
	"""
	
	print("\nPrinted models: ")
	
	for design in completed_models:
		print(design)
	


