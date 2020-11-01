def build_person(first, last, age='', location=''):
	"""Build a dictionary about someone"""
	person = {'first': first, 'last': last,}
	
	if age:
		person['age'] = age
	if location:
		person['location'] = location
		
	return person
	
human = build_person('alex', 'lin', age=15, location='lynnfield')
print(human)
