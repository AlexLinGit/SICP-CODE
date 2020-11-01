files = ['dogs.txt', 'cats.txt']

for a_file in files:
	try:
		with open(a_file) as t_file:
			print(t_file.read())
	except FileNotFoundError:
		pass
