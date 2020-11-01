from collections import OrderedDict

favorite_languages = OrderedDict()



favorite_languages['jen'] = ['python', 'smalltalk']
favorite_languages['josh'] = ['c++', 'lisp', 'pascal']
favorite_languages['jake'] = ['assembly',]
favorite_languages['todd'] = ['java', 'assembly']
favorite_languages['alex'] = ['c++',]
	



for name,languages in favorite_languages.items():
	if len(languages) > 1:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())
	else:
		print("\n" + name.title() + "'s favorite language is " + 
		language.title())
