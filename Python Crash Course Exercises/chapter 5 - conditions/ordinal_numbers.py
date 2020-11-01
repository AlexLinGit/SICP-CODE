ordinal = [1,2,3,4,5,6,7,8,9]

for ord in ordinal:
	if ord == 1:
		print(str(ord) + "st")
	elif ord == 2:
		print(str(ord) + "nd")
	elif ord == 3:
		print(str(ord) + "rd")
	else:
		print(str(ord) + "th")
