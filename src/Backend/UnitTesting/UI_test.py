from unittest import TestCase
import Backend
from Backend.Integration.mainpage import MainPage
from Backend.Integration.viewpage import ViewPage
from Backend.Integration.loadpage import LoadPage
from Backend.Integration.infopage import InfoPage

class TestUI(TestCase):

    def setUp(self):
        self.mainpage = MainPage(None, None, None)
        self.path = "src/Backend/UnitTesting/test_folder"
        self.files = ['MDRRW014dfr']
        self.finished = False
        self.max = 0
        self.answers = [{"Country": "Rwanda", "ISO": "RWA", "Admin1": "20RWA001 ", "Admin2": "20R053WA005053 ", "Start": "11 July 2017", 
             "End": "01 September 2017", "Glide": "ST-2017 -000035 -RWA", "OpNum": "MDRRW014", "OpBud": "CHF 49,122", 
             "Host": "Rwanda Red Cross Society", "Affected": 675, "Assisted": "811 households"}]

    def test_extract_answers(self):
        self.assertEqual(self.mainpage.get_files_in_folder(self.path), self.files[0])
        self.assertTrue(self.finished)

t = TestUI
t.test_extract_answers