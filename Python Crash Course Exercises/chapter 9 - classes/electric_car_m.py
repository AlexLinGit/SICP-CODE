from cars import Cars


class ElectricCar(Cars):
	"""Represents aspects specific to electric cars"""
	
	def __init__(self, make, model, year):
		"""Initializes attributes of the parent class"""
		super().__init__(model, make, year)
		self.battery = Battery()
		
	def fill_gas_tank(self):
		"""Electric cars don't use gas"""
		print("NO GAS REQUIRED!")


class Battery():
	"""Represents a battery"""
	
	def __init__(self, battery_size=70):
		"""Initializes battery size"""
		self.battery_size = battery_size
		self.plus_kwh = 0
		
	def read_battery(self):
		"""Prints a description of the battery"""
		print("Battery wattage: " + str(self.battery_size) + "-kwh")
	
	def upgrade_battery(self, plus_kwh):
		"""Upgrades the battery with number of kwh"""
		self.battery_size = self.battery_size + plus_kwh
	
	def car_range(self):
		"""Prints a approximate range which the car can drive"""
		if self.battery_size <= 70:
			car_range = "from 150 to 200 miles"
		elif self.battery_size <= 85:
			car_range = "from 200 to 300 miles"
		elif self.battery_size <=95:
			car_range = "above 300 miles"
		elif self.battery <= 0:
			car_range = "This doesn't move"
		else:
			car_range = "unknown"
			
		if car_range == 'unknown':
			print("The range of this car is undetermined")
		elif car_range == "this doesn't move":
			print(car_range)
		else:
			print("\nThis car can go " + car_range + 
			" away on a single charge of its ")
			print(str(self.battery_size) + "-kwh battery.")
			
