class AnonymousSurvey():
	"""Collects anonymous surveys responses and stores in list"""
	
	def __init__(self, question):
		"""Initializes question and response list"""
		self.question = question
		self.responses = []
		
	def show_responses(self):
		"""Shows the responses from the response list"""
		print("Responses:")
		for res in self.responses:
			print("- " + res  + " years old")
			
	def store_responses(self, response):
		"""Stores a response"""
		self.responses.append(response)
		
	def show_question(self):
		"""shows the survey question"""
		print("Question:")
		print("- " + self.question)
		
	
