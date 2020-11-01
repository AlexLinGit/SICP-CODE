import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test case for Employee class"""
	
	def setUp(self):
		"""Sets up an instance of Employee class"""
		self.josh = Employee(first='josh', last='peck', salary=200000)
		 
	def test_give_default_raise(self):
		"""Test if the default raise method works"""
		self.josh.give_raise()
		self.assertEqual(self.josh.salary, 205000)
		
	def test_give_custom_raise(self):
		"""Test if the custom raise works"""
		self.josh.give_raise(e_raise=100000)
		self.assertEqual(self.josh.salary, 300000)
		

unittest.main()
