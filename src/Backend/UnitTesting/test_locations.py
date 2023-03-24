import unittest 
from Integration.locations import Locations

class TesIntegration(unittest.TestCase):
    def setUp(self):
        self.file = "src/Backend/UnitTesting/MDRRW014dfr.pdf"
        self.locations = Locations(self.file)
        self.ans = self.locations.exctract_loc()


    def test_locations(self):
        actual = ['Gatsibo', 'the Eastern Province', 'Rwanda', 'Gatsibo District', 'Eastern Province', 'the City of Kigali']
        self.assertEquals(actual,self.ans)
        
if __name__ == '__main__' :         
    unittest.main()