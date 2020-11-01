import json 

filename = 'numbers.json'
with open(filename) as f_ob:
	numbers = json.load(f_ob)
	
print(numbers)

