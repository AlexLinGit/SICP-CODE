favorite_places = {
	'alex': ['home', 'villa', 'australia',],
	'mom': ['china', 'home', 'france',],
	'angelo': ['hell', 'purgatory', 'in misery',],
	}
	
for name, places in favorite_places.items():
	print(name.title() + ": ")
	for place in places:
		print("\t " + place.title())
