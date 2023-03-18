from unittest import TestCase
from Integration.QA_model import qaModel

class TestQAModel(TestCase):
    def setUp(self):
        self.file = "src/Backend/UnitTesting/MDRRW014dfr.pdf"
        self.qa = qaModel(self.file)
        self.ans = self.qa.answers

    def test_answer_extraction(self):
        actual_answers = {'What country did the disaster occur in?': 'Rwanda',
 'What is the operation start date?': '11 July 2017',
 'What is the operation end date?': '01 September 2017',
 'What is the number of people affected?': '675',
 'What is the number of people assisted?': '811 households',
 'What is the Glide Number?': 'ST-2017 -000035 -RWA',
 'What is the Operation n°?': 'MDRRW014',
 'What is the Operation Budget?': 'CHF 49,122',
 'What is the Host National Society?': 'Rwanda Red Cross Society'}
        self.assertEquals(actual_answers, self.ans)