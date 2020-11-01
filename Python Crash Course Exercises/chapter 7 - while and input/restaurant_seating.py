seating = input("How many people do you have? ")
seating = int(seating)

if seating > 8:
	print("Please wait by the waiting area to be served.")
elif seating < 0:
	print("Physch! That's the wrong number!")
else:
	print("We have an open table right over here!")
