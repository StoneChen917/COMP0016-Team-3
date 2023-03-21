import unittest 
from Integration import read_file
from UnitTesting import *
import magic
import PyPDF2
from PyPDF2 import PdfReader

class TestReadFile(unittest.TestCase):

    def setUp(self):
        file = "MDRRW014dfr.py"
        self.check_type(file)
        return self.test_read_file(file)

    def test_check_type(self):
        if ("PDF document" in magic.from_file(self.file)):
            return True
        else:
            raise ValueError("wrong type of file, pdf only")

    def test_read_file(self):
        test = read_file(self, self.file)
        self.assertEqual(self.test_read_file(), "Emergency Plan of Action Final Report Rwanda: Storm and Heavy Winds DREF operation Operation n° MDRRW014 Date of Issue: Glide number: ST-2017-000035-RWA Date of disaster: 01 April 2017 Operation start date: 11 July 2017 Operation end date: 01 September 2017 Host National Society: Rwanda Red Cross Society Operation budget: CHF 49,122 Number of people affected: 675 people (135 households) Number of people assisted: 811 households N° of National Societies involved in the operation: Belgian Red Cross Flanders, Austrian Red Cross, Belgian Red Cross French Community, Spanish Red Cross International Federation of Red Cross and Red Crescent Societies. N° of other partner organizations involved in the operation: Local Authorities, the Ministry of Disaster Management and Refugees Affairs (MIDIMAR) A. Situation analysis Description of the disaster On 01 April 2017 at 3:00 pm, Gatsibo district located in the Eastern Province of Rwanda experienced heavy rainfall associated with heavy storms, which resulted in destruction of houses and community farm lands in Kiramuruzi Sector Nyabisindu Cell. The affected area is located 36 kilometers from Gatsibo District, 40 kilometers from the Eastern Province office and 70 kilometers from the City of Kigali. The preliminary assessment gathered by Rwanda Red Cross staff and volunteers, estimated that 675 people (135 households) were affected by heavy wind and storms. Renewed assessments confirmed that the amount of people affected remained around 135 households. The last performed assessment in June, showed that households were impacted in the following way: • Households with houses destroyed and living with host communities (N= 34 households) • Households living in their destroyed houses (with half a roof) (N= 57 households) • Households that have recovered their houses and are managing (N= 44 households) • Households that need roofing for latrines (N= 811 households) House with roof destroyed in Gatsibo district ©IFRC ")


if __name__ == '__main__' :         
    unittest.main()
