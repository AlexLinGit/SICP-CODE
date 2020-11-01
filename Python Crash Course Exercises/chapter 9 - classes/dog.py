class Dog():
	"""simulates dogs"""
	
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age
	
	
	def sit(self):
		"""Simulate a dog sitting"""
		print(self.name.title() + " is now sitting.")
	
	
	def roll(self):
		"""Simulates a dog rolling over"""
		print(self.name.title() + " rolled over!")


my_dog = Dog('caca', 6)
print("I have a " + str(my_dog.age) + " year old dog named " + 
		my_dog.name.title() + ".")

my_dog.sit()
my_dog.roll()


your_dog = Dog('pitbull', 12)
print("\nI have a " + str(your_dog.age) + " year old dog named " + 
		your_dog.name.title() + ".")

your_dog.sit()
