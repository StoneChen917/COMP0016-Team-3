# IMPROVEMENTS WHEN FINALISED
    # unify file, first page, and rest of pages
    # make models take in text from here, from class attributes

import PyPDF2
import pandas as pd
import openpyxl
# import xlsxwriter


from QA_model import qaModel
from code_matching import codeMatch
from locations import Locations
from readfile import ReadFile
import os

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
        return answers
       
    
    def get_admin_0(self):
        country = self.get_answers()["What is the Country of Disaster?"]
        return country

    def get_ISO_code(self):
        fuzz = codeMatch(self.admin_0, self.loc_list)
        iso_code = fuzz.getISOCode()
        return iso_code

    def remove_admin_0(self):
        locations = Locations(self.file)
        lst = locations.exctract_loc()

        # remove admin 0
        if self.admin_0 in lst:
            lst.remove(self.admin_0)
        
        return lst
        
    def get_pcodes(self):
        fuzz = codeMatch(self.admin_0, self.loc_list)
        fuzz.loop_p_codes()
        self.admin_1_codes = fuzz.p_code_1
        self.admin_2_codes = fuzz.p_code_2
        return([fuzz.p_code_1, fuzz.p_code_2])
    
    def extract(self):
        final = {}
        # country
        final["Country"]=self.admin_0
        # iso
        final["ISO"]=self.ISO
        # admin 1(list of dictionary)
        final["Admin1"]=self.admin_1_codes
        # admin 2(list of dictionary)
        final["Admin2"]=self.admin_2_codes
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


def dict_parser(final,path):
    
        print(final)
        Country = final['Country']
        ISO = final['ISO']
        
        try:
            Admin1 = " "
            ad1len = len(final['Admin1'])
            for x in range(ad1len):
                result = final['Admin1'][x].get('P-Code')
                print(result)
                Admin1 = result + " "
            
            Admin2 = " "
            ad2len = len(final['Admin2'])
            for x in range(ad2len):
                result = final['Admin2'][x].get('P-Code')
                Admin2 = result + " "
        except:
            Admin1 = " "
            Admin2 = " "
        finally:
            Start = final['Start']
            End = final['End']
            Affected = final['Affected']
            Assisted = final['Assisted']
            Glide = final['Glide']
            OpNum = final['OpNum']
            OpBud = final['OpBud']
            Host = final['Host']        
            
            df = pd.read_excel('src/Backend/Integration/batchresults.xlsx')
            list_row = [path, Country, ISO, Admin1, Admin2,Start,End,Affected,Assisted,Glide,OpNum,OpBud,Host]
            #df = df.append(list_row, ignore_index=True )
            df = df.append(pd.Series(list_row, index=df.columns[:len(list_row)]), ignore_index=True)
            df.to_excel('src/Backend/Integration/batchresults.xlsx', index=False)


dir_path = r'C:\\Users\\zaynb\\Documents\\COMP0016-Team-3\\sampledocs'
docs = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        docs.append("sampledocs/" + path)

for x in docs:
    path = x
    test = main(path)
    dict_parser(test.final_extract,path)

    
# test = main("src/Backend/Integration/testfile.pdf")
#path = "src/Backend/Integration/MDRKH001final.pdf"
#test = main(path)
#file_num = 1 #edit
#print(test.final_extract)
##dict_parser(test.final_extract,path)
# test_dict = {'Country': 'Rwanda', 'ISO': 'RWA', 'Admin1': [{'Location': 'Eastern Province', 'P-Code': '20RWA005'}, {'Location': 'the City of Kigali', 'P-Code': '20RWA001'}], 'Admin2': [{'Location': 'Flanders', 'P-Code': '20RWA004042'}, {'Location': 'Gatsibo district', 'P-Code': '20RWA005053'}, {'Location': 'Gatsibo District', 'P-Code': '20RWA005053'}, {'Location': 'Gatsibo d istrict \n©IFRC', 'P-Code': '20R053WA005053'}], 'Start': '11 July 2017', 'End': '01 September 2017', 'Affected': '675', 'Assisted': '811 households', 'Glide': 'ST-2017 -000035 -RWA', 'OpNum': 'MDRRW014', 'OpBud': 'CHF 49,122', 'Host': 'Rwanda Red Cross Society'}
# dict_parser(test_dict,path)
# print(test.loc_list)
# print(test.get_admin_0)
# print(test.final_extract)
# print("admin 0: " + test.admin_0)
# print(f"ISO code: {test.ISO}" )
# # test.get_pcodes()
# print(f"admin1 codes: {test.admin_1_codes}")
# print(f"admin2 codes: {test.admin_2_codes}")
