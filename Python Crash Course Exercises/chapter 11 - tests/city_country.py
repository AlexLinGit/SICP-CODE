def city_names(city, country, population=""):
	"""Formats a city name and its country"""
	if population:
		formatted = city.title() + ", " + country.title() 
		formatted += " - Population: " + str(population)
	else:
		formatted = city.title() + ", " + country.title() 
	print(formatted + "\n")
	return formatted
	

