from survey import AnonymousSurvey

question = "How old are you?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Press 'q' to quit")
while True:
	feedback = input("Age:  ")
	if feedback == 'q':
		break
	my_survey.store_responses(feedback)
	
print("\nHere are the survey results")
my_survey.show_responses()
