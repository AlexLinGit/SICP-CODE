"""Class representing a car"""


class Cars():
	"""Simple class to represent car"""
	
	def __init__(self, model, make, year,):
		"""Initialize car attributes"""
		self.model = model
		self.make = make
		self.year = year
		self.miles = 0
	
	def summary(self):
		"""Prints a summary of car info"""
		full_summary = str(self.year) + " " + self.make + " " +  self.model
		return full_summary.title()
		
	def odometer_reading(self):
		"""Prints the miles on a car"""
		print("\nThis car had " + str(self.miles) + " miles.")
		
	def update_odometer(self, mileage):
		"""Updates the miles"""
		if mileage >= self.miles:
			self.miles = mileage
		else:
			print("\nYOU CAN'T ROLL BACK AN ODOMETER")
		
	def increment_odometer(self, mile_driven):
		"""Increments the mileage"""
		if mile_driven >= 0:
			self.miles += mile_driven
		else:
			print("\nStop trying to change the odometer")



			
	

