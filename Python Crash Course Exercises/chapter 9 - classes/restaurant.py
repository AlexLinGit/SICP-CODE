class Restaurants():
	"""
	Creates restaurant with name, cuisine type
	Prints out info
	Opens a restaurant instance
	"""
	
	def __init__(self, name, cuisine_type):
		"""Initialize name and cuisine attributes"""
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def print_info(self):
		"""Prints the restaurant's info"""
		print(self.name.title() + "-")
		print("Cuisine: " + self.cuisine_type)
		
	def status(self):
		"""Prints that the restaurant is open"""
		print(self.name.title() + " is now open.")
	
	def customers(self):
		"""Prints the number of people served"""
		print(self.name.title() + " has served " + str(self.number_served) +
				" people.")
		
	def set_served(self, customers):
		"""Sets the number of customers served"""
		self.number_served = customers

	def increment_served(self, more):
		"""Adds on more people who have been served"""
		if more >= 0:
			self.number_served += more
		else:
			print("You can't unserve someone")


class IceCreamStand(Restaurants):
	"""Represents certain aspects of an ice cream stand"""
	
	def __init__(self, name, cuisine_type):
		"""Initializes the name, cuisine, and flavors attributes"""
		super().__init__(name, cuisine_type)
		self.flavors = []
		
	def menu(self):
		"""Prints a menu of the ice cream flavors available"""
		print(self.name.title() + "'s menu: ")
		for flavor in self.flavors:
			print(" \t-" + flavor)
		

