from collections import OrderedDict

glossary = OrderedDict()


glossary['.pop']= 'removes item in list, but still can be worked with'
glossary['syntax']= 'the way which languages must be written'
glossary['loops']= 'loops through a list or dictionary'
glossary['abstraction']= 'the way a problem is percieved through a programmer'
glossary['interface']= 'what the user interacts with'
glossary['set()']= 'creates a list of unique values'
	
	
for definition in glossary:
	print(definition.title() + ": " + glossary[definition] + "\n")
