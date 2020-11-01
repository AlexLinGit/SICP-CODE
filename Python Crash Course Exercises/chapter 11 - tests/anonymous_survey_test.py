import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Test case for AnonymousSurvey class"""
	
	def setUp(self):
		"""Set up for AnonymousServer instance"""
		question = "Where are you?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['Lynnfield', 'Boston', 'Cambridge']
	
	
	def test_store_single_response(self):
		"""Does a single response store properly?"""
		self.my_survey.store_responses(self.responses[0])
		self.assertIn("Lynnfield", self.my_survey.responses)
	
	def test_store_multiple_responses(self):
		"""Do multiple responses store properly?"""
		for res in self.responses:
			self.my_survey.store_responses(res)
			self.assertIn(res, self.my_survey.responses)
	
unittest.main() 
