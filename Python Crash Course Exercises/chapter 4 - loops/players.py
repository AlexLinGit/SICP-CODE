players = ['marta', 'eli', 'alex', 'joe', 'josh']
print(players[-3:])

print("My players:")
for player in players[2:]:
	print(player.title())

print("First three items are:\n", players[:3])
print("\nThree items from middle are:\n", players[1:4])
print("\nLast three items are:\n", players[2:])
