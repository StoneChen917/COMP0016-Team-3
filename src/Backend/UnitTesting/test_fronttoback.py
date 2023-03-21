import unittest 
from Integration import fronttoback

class TestFrontoback(unittest.TestCase):

    def setUp(self):
        self.files = ['MDRRW014dfr']
        self.finished = False
        self.max = 0
        self.answers = [{"Country": "Rwanda", "ISO": "RWA", "Admin1": "20RWA001 ", "Admin2": "20R053WA005053 ", "Start": "11 July 2017", 
             "End": "01 September 2017", "Glide": "ST-2017 -000035 -RWA", "OpNum": "MDRRW014", "OpBud": "CHF 49,122", 
             "Host": "Rwanda Red Cross Society", "Affected": 675, "Assisted": "811 households"}]

    def test_extract_answers(self):
        self.assertEqual(len(self.answers), self.max + 1)
        self.assertTrue(self.finished)

    def test_reset_ftb(self):
        self.assertFalse(self.fb.finished)

    def test_is_finished(self):
        self.fail()

    def test_get_files(self):
        return self.files

    def test_get_answers(self):
        return self.answers
    
    def test_get_max(self):
        return self.max

    def test_set_files(self):
        for file in self.files:
            self.files.append(file)

    def test_get_admin0(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_admin0(1), "Rwanda")

    def test_get_iso(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_iso(1), "RWA")

    def test_get_admin1(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_admin1(1), "20RWA001")

    def test_get_admin2(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_admin2(1), "20R053WA005053")

    def test_get_start(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_start(1), "11 July 2017")

    def test_get_end(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_end(1), "01 September 2017")

    def test_get_glide(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_glide(1), "ST-2017 -000035 -RWA")

    def test_get_operation_number(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_operation_number(1), "MDRRW014")

    def test_get_operation_budget(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_operation_budget(1), "CHF 49,122")

    def test_get_host(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_host(1), "Rwanda Red Cross Society")

    def test_get_affected(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_affected(1), "675")

    def test_get_assisted(self):
        self.test_extract_answers()
        self.assertEqual(self.test_get_assisted(1), "811 households")

if __name__ == '__main__' :         
    unittest.main()