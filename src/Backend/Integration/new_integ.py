# IMPROVEMENTS WHEN FINALISED
    # unify file, first page, and rest of pages
    # make models take in text from here, from class attributes

import PyPDF2
from readfile import ReadFile
from QA_model import qaModel
from cosine import Cosine
from locations import Locations

class main():
    def __init__(self, file):
        self.file=file
        self.reader = ReadFile()
        # self.locations=Locations(file)
        self.admin_0 = self.get_admin_0()
        self.first_page = self.get_first_page()
        self.other_pages = self.get_other_pages()
        self.loc_list = self.remove_admin_0()
        self.admin_1_codes = None
        self.admin_2_codes = None
        self.get_pcodes()
        self.ISO = self.get_ISO_code()

        # answers to quest

    

    def get_first_page(self):
        # reader = ReadFile()
        
        self.first_page = self.reader.exec(self.file)[0]
    
    def get_other_pages(self):
        # reader = ReadFile()
        self.other_pages = self.reader.exec(self.file)[1]
    
    def get_answers(self):
       answers=qaModel(self.file).answers
       return answers
    
    def get_admin_0(self):
        country = self.get_answers()["What is the Country of Disaster?"]
        return country

    def get_ISO_code(self):
        cosine = Cosine(self.admin_0, self.loc_list)
        iso_code = cosine.getISOCode()
        return iso_code

    def remove_admin_0(self):
        locations = Locations(self.file)
        lst = locations.exctract_loc()
        # print(lst)

        # remove admin 0
        if self.admin_0 in lst:
            lst.remove(self.admin_0)
        
        return lst
        
    def get_pcodes(self):
        cosine = Cosine(self.admin_0, self.loc_list)
        self.admin_1_codes = cosine.p_code_1
        self.admin_2_codes = cosine.p_code_2
        # return(list(admin_1,admin_2))


# test = main("src/Backend/Integration/testfile.pdf")
test = main("src/Backend/Integration/MDRKH001final.pdf")

print(test.loc_list)
print("admin 0:"+test.admin_0)
print("ISO CODE:"+test.ISO)
print(test.admin_1_codes)
print(test.admin_2_codes)