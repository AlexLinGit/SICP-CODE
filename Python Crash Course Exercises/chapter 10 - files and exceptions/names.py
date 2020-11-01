from name_function import get_formatted_name

print("Press 'q' to quit")
while True:
	first = input("Enter your first name:  ")
	if first == 'q':
		break
	
	last = input("Enter your last name:  ")
	if last == 'q':
		break
	
	full = get_formatted_name(first, last)
	print("\tFormatted name: " + full + "\n" )
