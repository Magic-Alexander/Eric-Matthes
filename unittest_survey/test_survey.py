import unittest

from survey import AnonimousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):

        question = "What language did you first learn to speak?"
        self.my_survey = AnonimousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
 





if __name__ == '__main__':
    unittest.main()