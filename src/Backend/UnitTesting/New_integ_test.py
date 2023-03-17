from unittest import TestCase
from Integration.new_integ import main




class TesIntegration(TestCase):
    def setUp(self):
        self.file = "src/Backend/UnitTesting/MDRRW014dfr.pdf"
        self.integ = main(self.file)
        self.ans = self.integ.final_extract


    def test_first_page(self):
        pass

    def test_answers(self):
        actual = {'Country': 'Rwanda', 'ISO': 'RWA', 'Admin1': [{'Location': 'Eastern Province', 'P-Code': '20RWA005'}, {'Location': 'the City of Kigali', 'P-Code': '20RWA001'}], 'Admin2': [{'Location': 'Gatsibo', 'P-Code': '20RWA005053'}], 'Start': '11 July 2017', 'End': '01 September 2017', 'Affected': '675', 'Assisted': '811 households', 'Glide': 'ST-2017 -000035 -RWA', 'OpNum': 'MDRRW014', 'OpBud': 'CHF 49,122', 'Host': 'Rwanda Red Cross Society'}
        self.assertAlmostEquals(actual,self.ans)
