import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Test for get_formatted_name function"""
	
	def test_first_last_name(self):
		"""Do first and last names work?"""
		formatted_name = get_formatted_name('bruce', 'lee')
		self.assertEqual(formatted_name, 'Bruce Lee')
		
	def test_first_middle_last_name(self):
		"""Fo first, middle, and last names work"""
		formatted_name = get_formatted_name('bill', 'bob', middle='nmn')
		self.assertEqual(formatted_name, 'Bill Nmn Bob')
		
unittest.main()
