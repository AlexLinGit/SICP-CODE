pi_file = 'C:\\Users\\Alex\\desktop\\python_work\\Text_Files\\' 
pi_file += 'Project_Related\\pi_million_digits.txt'

with open(pi_file) as pi_object:
	lines = pi_object.readlines()

pi_s = ''
for line in lines:
	pi_s += line.strip()
	
birthday = input("Type your birthday in mmddyy:  ")
if birthday in pi_s:
	print("Your birthday is in pi!")
else:
	print("Nothing so far...")
	
