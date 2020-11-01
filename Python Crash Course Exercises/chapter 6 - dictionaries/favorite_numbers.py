favorite_numbers = {
	'alex': [64, 73,],
	'mom': [0, 12,],
	'angelo': [9000, 666],
	'sheldon': [73, 667,],
	}

for name, number in favorite_numbers.items():
	print(name.title() + ": ")
	for num in number:
		print(" \t " + str(num)) 
