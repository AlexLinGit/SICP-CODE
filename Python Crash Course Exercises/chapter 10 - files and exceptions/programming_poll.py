filename = 'cs_poll.txt'

cs_result = {}

while True:
	name = input("\nWhat is your name?   \n")
	if name == 'stop':
		break
	
	reason = input("Why do you like to program?  \n")
	if reason == 'stop':
		break
	
	cs_result[name] = reason
	
	with open(filename, 'a') as poll:
		for name, reason in cs_result.items():
			poll.write("\n" + name.title() + ":\n")
			poll.write("\t  " + reason + "\n")
	
	
