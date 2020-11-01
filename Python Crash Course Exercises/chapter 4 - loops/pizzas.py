pizzas = ['cheese', 'mushrooms', 'chicken']
for pizza in pizzas:
	print("One of my favorite pizzas toppings is " + pizza.title() + "!")

print("You know, I really, really like pizza.  Especially " + pizza.title() + " pizza!")

friends_pizzas = pizzas[:]

pizzas.append('anchioves')
friends_pizzas.append('pepperoni')

print("\nMy pizzas\n", pizzas)
print("\nFriend's pizzas\n", friends_pizzas)

pizzaone = {
	'toppings': ['mushrooms', 'pineapple', 'ham'],
	'crust': 'medium',
	}

print("  \n")

print("You ordered a " + pizzaone['crust'] + "and the following toppings:")
for top in pizzaone['toppings']:
	print("\t" + top.title())
	
