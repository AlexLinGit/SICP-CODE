def show_magicians(names):
	"""
	Greets magicians in a list
	"""
	for name in names:
		print(name.title())		
		
		
def make_great(names):
	"""
	Adds 'make great' to the end of names
	"""
	for i in range(len(names)):
		names[i] += ' the Great'
		
