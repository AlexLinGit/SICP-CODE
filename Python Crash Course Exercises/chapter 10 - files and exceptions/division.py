print("Give me two numbers and I will divide them")
print("(press 'q' to stop anytimee)")

while True:
	first = input("\nFirst number: ")
	if first == 'q':
		break
		
	second = input("Second number: ")
	if second == 'q':
		break
	
	try:
		answer = int(first)/int(second)
	except ZeroDivisionError:
		print("You can't divide by zero!") 
	except ValueError:
		print("Please enter a number")
	else:
		print(answer)




