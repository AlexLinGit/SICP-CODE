def make_sandwich(*ingrediants):
	"""Summarizes sub ingrediants"""
	print("\nSub ingrediants: ")
	for ingrediant in ingrediants:
		print("- " + ingrediant)
		

make_sandwich('turkey', 'cheese')
make_sandwich('beef', 'cheese', 'mushrooms')
