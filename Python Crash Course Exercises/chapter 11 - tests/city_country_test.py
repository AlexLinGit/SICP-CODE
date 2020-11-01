import unittest
from city_country import city_names

class CityCountryTestCase(unittest.TestCase):
	"""Test for 'city_country' function"""
	
	def test_city_country(self):
		"""Do 'city, country' work?"""
		test = city_names(city='boston', country='united states')
		self.assertEqual(test, 'Boston, United States')
		
	def test_city_country_populatio(self):
		"""Does population work?"""
		test = city_names(city="boston", population=1000000, 
		country='united states')
		self.assertEqual(test, 'Boston, United States - Population: 1000000') 
		
		
unittest.main()
