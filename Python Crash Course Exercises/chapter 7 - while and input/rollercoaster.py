height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("You are eligible to ride!")
elif height <= 0:
	print("Ain't no one that short.  Enter a new value.")
else: 
	print("You are too short, midget!")
