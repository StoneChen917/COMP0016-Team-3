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
        self.final_extract=self.extract()




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
    
    def extract(self):
        final = {}
        # country
        final["Country"]=self.admin_0
        # iso
        final["ISO"]=self.ISO
        # admin 1(list of dictionary)
        final["Admin1"]=self.admin_1_codes
        # admin 2(list of dictionary)
        final["Admin1"]=self.admin_2_codes
        # start date
        final["Start"]=self.get_answers()["What is the Operation Start Date?"]
        # end date
        final["End"]=self.get_answers()["What is the Operation End Date?"]
        # affected
        final["Affected"]=self.get_answers()["What is the number of people affected?"]
        # assisted
        final["Assisted"]=self.get_answers()["What is the number of people assisted?"]
        # glide
        final["Glide"]=self.get_answers()["What is the Glide Number?"]
        # operation number
        final["OpNum"]=self.get_answers()["What is the Operation n°?"]
        # operation budget
        final["OpBud"]=self.get_answers()["What is the Operation Budget?"]
        # host national society
        final["Host"]=self.get_answers()["What is the Host National Society?"]

        return final




# test = main("src/Backend/Integration/testfile.pdf")
path = "src/Backend/Integration/MDRRW014dfr.pdf"
test = main(path)
print(test.final_extract)

# # print(test.loc_list)
# print("admin 0: " + test.admin_0)
# print(f"ISO code: {test.ISO}" )
# # test.get_pcodes()
# print(f"admin1 codes: {test.admin_1_codes}")
# print(f"admin2 codes: {test.admin_2_codes}")
