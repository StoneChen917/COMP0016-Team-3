# import psycopg2



hostname = "localhost"
database = "cifrc"
username = "postgres"
pwd = "Abc123456"
port_id = 5433
conn = None
cur = None

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
    """Main class that integrates all the extraction. All extracted information are stored in self.final_extract"""
    def __init__(self, file):
        self.file=file
        self.reader = ReadFile()
        self.admin_0 = self.get_admin_0()
        self.first_page = self.get_first_page()
        self.other_pages = self.get_other_pages()
        self.loc_list = self.remove_admin_0()
        self.admin_1_codes = self.get_pcodes()[0]
        self.admin_2_codes = self.get_pcodes()[1]
        self.ISO = self.get_ISO_code()
        self.final_extract=self.extract()




    def get_first_page(self):
        self.first_page = self.reader.exec(self.file)[0]
    
    def get_other_pages(self):
        self.other_pages = self.reader.exec(self.file)[1]
    
    def get_answers(self):
        # QA model answers
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


def dict_parser(final,path,list_answers):
    
        Country = final['Country']
        ISO = final['ISO']
        
        Admin1 = " "
        ad1len = len(final['Admin1'])
        for x in range(ad1len):
            result = final['Admin1'][x].get('P-Code')
            if result != "None":
                Admin1 = Admin1 + result + " "

        Admin2 = " "
        ad2len = len(final['Admin2'])
        for x in range(ad2len):
            result = final['Admin2'][x].get('P-Code')
            if result != "None":
                Admin2 = Admin2 + result + " "

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
        doc_ans = {'path' : path, 'Country' : Country, 'ISO' : ISO, 'Admin1' : Admin1, 'Admin2' : Admin2,'Start' : Start,'End' : End,'Affected' : Affected,'Assisted' : Assisted,'Glide' : Glide,'OpNum': OpNum,'OpBud' : OpBud,'Host' : Host}
        #df = df.append(list_row, ignore_index=True )
        list_answers.append(doc_ans)
        df = df.append(pd.Series(list_row, index=df.columns[:len(list_row)]), ignore_index=True)
        df.to_excel('src/Backend/Integration/batchresults.xlsx', index=False)

def front_integ(docs):
    list_answers = []
    for x in docs:
        path = x
        test = main(path)
        dict_parser(test.final_extract,path,list_answers)
    return list_answers
