def build_car(model, manufacturer, **car_info):
	"""
	Builds a profile of a car
	"""
	car_profile = {}
	car_profile['model'] = model
	car_profile['manufacturer'] = manufacturer
	
	for key, value in car_info.items():
		car_profile[key] = value
		
	return car_profile
	
my_car = build_car('electric hybrid', 'tesla', condition='new', 
				year=2017)
		
print(my_car)
