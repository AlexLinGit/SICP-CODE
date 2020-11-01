rivers = {
		'nile': 'egypt',
		'amazon': 'brazil',
		'huanghe': 'china',}
		  
for river, country in rivers.items():
	print("The " + river.title() + " river runs through " + country.title() +
	".")
	print(river.title() + ", " + country.title() + "\n")
