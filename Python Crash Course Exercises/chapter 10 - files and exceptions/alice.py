def count_words(filename):
	"""Counts the words in a file"""
	try:
		with open(filename) as f_ob:
			contents = f_ob.read()
	except FileNotFoundError:
		print(filename + " does not exist or isn't in this directory")
	else:
		words = contents.split()
		num_words = len(words)
		print(filename + " has ~" + str(num_words) + " words")
	

filename = ['alice.txt', 'little_women.txt', 'siddhartha.txt', 
		'moby_dick.txt']

for file in filename:
	count_words(file)
