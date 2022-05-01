from class_to_test import AnonymousSurvey
import unittest


class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "lang? "
        my_survey = AnonymousSurvey(question)
        response = "English"
        my_survey.store_response(response)
        self.assertIn("English", my_survey.responses)

    def test_store_three_responses(self):
        question = "langs? "
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Spanish", "Portuguese"]

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()


"""
# class to be tested

question = "what lang did you learn first?"

my_survey = AnonymousSurvey(question)

my_survey.show_question()

while True:
    response = input("lang: ")
    if response == "q":
        break
    my_survey.store_response(response)

my_survey.show_results()

"""
