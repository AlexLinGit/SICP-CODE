favorite_languages = {
	'jen': ['python', 'smalltalk'],
	'josh': ['c++', 'lisp', 'pascal'],
	'jake': ['assembly',],
	'todd': ['java', 'assembly'],
	'alex': ['c++',],
	}

for name, language in favorite_languages.items():
	for languag in language:
		print(name.title() + ": " + languag.title())

print(' \n') 

friends = ['jen', 'josh']
for name in sorted(favorite_languages.keys()):
	if name in friends:
		print("Hey " + name.title() + "! You like to code in " +
			favorite_languages[name].title() + "?")
	else:
		print(name.title())
			
if 'erin' not in favorite_languages.keys():
	print("\nErin, what is is your favorite language?")
	
print("  ")	
for language in set(sorted(favorite_languages.values())):
	print(language.title())

print("   ")
should_take = ['josh', 'caitlin', 'mia', 'dora']
for shoulds in should_take:
	if shoulds in favorite_languages:
		print(shoulds.title() + ", thanks for taking the survey!")
	else:
		print(shoulds.title() + ", why haven't you taken the survey yet?")

