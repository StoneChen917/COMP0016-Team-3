import unittest
from QA_model import qaModel

class TestQAModel(unittest.TestCase):
    def setUp(self):
        self.file = r"C:\Users\Santhosh\Downloads\MDRYE001final (1).pdf"
        self.qa = qaModel(self.file)
        self.ans = self.qa.answers

    def test_answer_extraction(self):
        actual_answers = {'What is the Country of Disaster?': 'Rwanda', 'What is the Operation Start Date?': '11 July 2017', 'What is the Operation End Date?': '01 September 2017', 'What is the number of people affected?': '675', 'What is the number of people assisted?': '811 households', 'What is the Glide Number?': 'ST-2017 -000035 -RWA', 'What is the Operation n°?': 'MDRRW014', 'What is the Operation Budget?': 'CHF 49,122', 'What is the Host National Society?': 'Rwanda Red Cross Society'}
        self.assertEquals(actual_answers, self.ans)
    
    #When some info is missing, the model extracts the next best answer instead of returning an empty string
    def test_answer_extraction_when_information_is_missing(self):
        actual_glide_number = ""
        extracted_glide_number = self.ans[5]
        self.assertFalse(actual_glide_number, extracted_glide_number)

if __name__ == '__main__' :         
    unittest.main()