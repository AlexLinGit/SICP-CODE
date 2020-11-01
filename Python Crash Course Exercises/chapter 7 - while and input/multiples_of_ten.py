number = "Give me a number "
number += "and I will tell you if it is a multiple of ten "
numbers = input(number)
numbers = int(numbers)

if numbers < 0:
	print("Not a multiple of ten!")
elif numbers % 10 == 0:
	print("Multiple of ten!")
else:
	print("Not a multiple of ten!")
