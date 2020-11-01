my_foods = ['pork belly', 'ice-cream', 'food']
friend_foods = my_foods[:]

my_foods.append('grapes')
friend_foods.append('oranges')

print(my_foods)
print(friend_foods)

for food in my_foods:
	print(food)
	
for food_one in friend_foods:
	print(food_one)
