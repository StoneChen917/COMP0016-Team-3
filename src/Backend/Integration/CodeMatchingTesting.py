import unittest
from code_matching import codeMatch

class TestCodeMatching(unittest.TestCase):
    def setUp(self):
        pass

    def test_admin0_exact_loc_name(self):
        self.admin_0 = 'India'
        self.code_match_admin0 = codeMatch(self.admin_0, [])
        self.admin0code = self.code_match_admin0.ISO_code
        expected_admin0code = "IND"

        self.assertEqual(expected_admin0code, self.admin0code)

    def test_admin0_fuzzymatching(self):
        self.admin_0 = 'Ruanda'
        self.code_match_admin0 = codeMatch(self.admin_0, [])
        self.admin0code = self.code_match_admin0.ISO_code
        expected_admin0code = "RWA"

        self.assertEqual(expected_admin0code, self.admin0code)

    def test_admin1_exact_loc_name(self):
        self.admin_1 = ["Qinghai", "Shandong", "Anhui"]
        self.code_match_admin1 = codeMatch("China", self.admin_1)
        self.code_match_admin1.loop_p_codes()
        expected_pcode1_values_exact = [{'Location': 'Qinghai', 'P-Code': '21CHN023'}, {'Location': 'Shandong', 'P-Code': '21CHN025'}, {'Location': 'Anhui', 'P-Code': '21CHN001'}]

        self.assertEqual(expected_pcode1_values_exact,self.code_match_admin1.p_code_1)

    def test_admin1_fuzzymatching(self):
        self.admin_1 = ["Al Dhale", "Sana", "Hadhramaut"]
        self.code_match_admin1 = codeMatch("Yemen", self.admin_1)
        self.code_match_admin1.loop_p_codes()
        expected_pcode_values = [{'Location': 'Al Dhale', 'P-Code': '20YEM030'}, {'Location': 'Sana', 'P-Code': '20YEM023'}, {'Location': 'Hadhramaut', 'P-Code': '20YEM019'}]

        self.assertEqual(expected_pcode_values,self.code_match_admin1.p_code_1)


    def test_admin2_exact_loc_name(self):
        self.admin_2 = ["Aisne", "Calvados", "Gironde"]
        self.code_match_admin1 = codeMatch("France", self.admin_2)
        self.code_match_admin1.loop_p_codes()
        expected_pcode_values = [{'Location': 'Aisne', 'P-Code': '20FRA007001'}, {'Location': 'Calvados', 'P-Code': '20FRA009001'}, {'Location': 'Gironde', 'P-Code': '20FRA010007'}]

        self.assertEqual(expected_pcode_values,self.code_match_admin1.p_code_2)


    def test_admin2_fuzzymatching(self):
        '''25014, 29001, 20007'''
        self.admin_2 = ["Al Hawtaa", "Harff Sufyaan", "Wosab AL-Alsafel"]
        self.code_match_admin1 = codeMatch("Yemen", self.admin_2)
        self.code_match_admin1.loop_p_codes()
        expected_pcode_values = [{'Location': 'Al Hawtaa', 'P-Code': '20YEM025014'}, {'Location': 'Harff Sufyaan', 'P-Code': '20YEM029001'}, {'Location': 'Wosab AL-Alsafel', 'P-Code': '20YEM020007'}]

        self.assertEqual(expected_pcode_values,self.code_match_admin1.p_code_2)


if __name__ == '__main__' :         
    unittest.main()