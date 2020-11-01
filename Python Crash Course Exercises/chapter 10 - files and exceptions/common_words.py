def count_spec_word(filename, words=[]):
	"""Count the appearance of certain words in text file"""
	with open(filename) as a_file:
		text= ''
		contents = a_file.readlines()
		for content in contents:
			text += content
		
		for word in words:
			print(text.lower().count(word))
	
		
count_spec_word('siddhartha.txt', words=['the', 'shit', 'him', 'fuck', 
										'indian', 'alex', 'goankar'])
		
