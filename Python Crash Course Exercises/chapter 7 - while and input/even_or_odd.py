number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number == 0:
	print("Neither!")
elif number % 2 == 0:
	print("It's even!")
else:
	print("Odd!")
