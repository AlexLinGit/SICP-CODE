requested_toppings =[]

available_toppings = ('mushrooms', 'cheese',
						'pepperoni', 'anchioves', 
						'pepper')
						
if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_toppings == 'chicken':
			print("No " + requested_topping + ".")
		elif requested_topping in available_toppings:
			print("Adding " + requested_topping + ".")
		else:
			print("We don't have " + requested_topping + ".")
	print("Pizza is done!")
else:
	print("Plain cheese pizza?")





	

