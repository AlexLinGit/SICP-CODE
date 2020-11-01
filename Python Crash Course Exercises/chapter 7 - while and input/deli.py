sandwich_orders = ['cheese & ham', 'bologna', 'bread', 'italian',
				'pastrami', 'pastrami', 'pastrami',]

finished_sandwiches = []

while sandwich_orders:
	if 'pastrami' in sandwich_orders:
		sandwich_orders.remove('pastrami')
		print("We are out of pastrami.")
	
	else:
		made = sandwich_orders.pop()
		finished_sandwiches.append(made)
		print("I am making your " + made + " sandwich.")
	
		

print(" \n")

for sandwich in finished_sandwiches:
	print("I made your " + sandwich + " sandwich.")
	
