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
        self.admin_1_codes = self.get_pcodes()[0]
        self.admin_2_codes = self.get_pcodes()[1]
        # self.get_pcodes()
        self.ISO = self.get_ISO_code()



    def get_first_page(self):
        # reader = ReadFile()
        
        self.first_page = self.reader.exec(self.file)[0]
    
    def get_other_pages(self):
        # reader = ReadFile()
        self.other_pages = self.reader.exec(self.file)[1]
    
    def get_answers(self):
       answers=qaModel(self.file).answers
       print(answers)
       return answers
       
    
    def get_admin_0(self):
        country = self.get_answers()["What is the Country of Disaster?"]
        print(country)
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
        cosine.loop_p_codes()
        self.admin_1_codes = cosine.p_code_1
        self.admin_2_codes = cosine.p_code_2
        # print(type(cosine.p_code_1),cosine.p_code_1)
        # print(type(cosine.p_code_2),cosine.p_code_2)
        return([cosine.p_code_1,cosine.p_code_2])


# test = main("src/Backend/Integration/testfile.pdf")
path = "src/Backend/Integration/MDRRW014dfr.pdf"
test = main(path)

# print(test.loc_list)
print("admin 0: " + test.admin_0)
print(f"ISO code: {test.ISO}" )
# test.get_pcodes()
print(f"admin1 codes: {test.admin_1_codes}")
print(f"admin2 codes: {test.admin_2_codes}")
