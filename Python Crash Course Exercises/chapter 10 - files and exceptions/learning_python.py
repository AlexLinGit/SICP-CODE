learn_p = 'C:\\Users\\Alex\\desktop\\python_work\\Text_Files\\'
learn_p += 'Project_Related\\learning_python.txt'

with open(learn_p) as python:
	pyth = python.readlines()

pyt = ''
for py in pyth:
	pyt += py
	
pyt = pyt.replace('Python', 'C')
print(pyt)

	
