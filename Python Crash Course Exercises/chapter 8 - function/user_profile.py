def build_profile(first, last, **user_info):
	"""Builds a user profile"""
	profile = {}
	profile['first'] = first
	profile['last'] = last
	
	for key, value in user_info.items():
		profile[key] = value
		
	return profile
	

alex_profile = build_profile(first='alex', last='lin', location='lynnfield', 
			favorite_subject='computer science', school='LMS')

print(alex_profile)
