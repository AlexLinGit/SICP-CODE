class Employee():
	"""Displays info on employee and also gives raises"""
	
	def __init__(self, first, last, salary):
		"""initializes name and salary"""
		self.first = first
		self.last = last
		self.salary = salary
		
	def show_info(self):
		"""Shows info on certain employee"""
		name = first.title() + " " + last.title()
		print(name + ": ")
		print("Salary: $" + str(salary) + "/year")
		
	def give_raise(self, e_raise=0):
		"""Gives default or custom raises"""
		if e_raise == 0:
			self.salary += 5000
		else:
			self.salary += e_raise
			
			
