def get_formatted_name(first, last, middle=''):
	"""Returns a neat full name"""
	if middle:
		full = first + ' ' + middle + ' ' + last
	else:
		full = first + ' ' + last
		
	return full.title()

while True:
	print("Please enter your name.")
	print("(Press q to quit at anytime")
	
	f_name = input("First name:  ")
	if f_name == 'q':
		break
	
	l_name = input("Last name:  ")
	if l_name == 'q':
		break
		
	m_name = input("Middle name (type none is you don't have one):  ")
	if m_name == 'q':
		break
	elif m_name == 'none':
		m_name = ''
		
	f_name = get_formatted_name(f_name, l_name, m_name)
	
	print("\nHi " + f_name.title() + "!\n")

	
	
	

