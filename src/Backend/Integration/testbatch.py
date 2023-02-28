import pandas as pd

def dict_parser(final,path):
       # for item in final.items():

        Country = final['Country']
        ISO = final['ISO']
        
        Admin1 = " "
        ad1len = len(final['Admin1'])
        for x in range(ad1len):
            result = final['Admin1'][x].get('P-Code')
            Admin1 = result + " "
        
        Admin2 = " "
        ad2len = len(final['Admin2'])
        for x in range(ad2len):
            result = final['Admin2'][x].get('P-Code')
            Admin2 = result + " "
        
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
        df = df.append(list_row, ignore_index=True )
        #df = df.append(pd.Series(list_row, index=df.columns[:len(list_row)]), ignore_index=True)
        df.to_excel('src/Backend/Integration/batchresults.xlsx', index=False)
'''         workbook = xlsxwriter.Workbook('src/Backend/Integration/Results_batch.xlsx')
        worksheet = workbook.add_worksheet("Sheet 1")

        ans = (
            [path, Country, ISO, Admin1, Admin2,Start,End,Affected,Assisted,Glide,OpNum,OpBud,Host]
        )
        row = 0 + file_num
        col = 0

        for path, Country, ISO, Admin1, Admin2,Start,End,Affected,Assisted,Glide,OpNum,OpBud,Host in (ans):
            worksheet.write(row, col, path)
            worksheet.write(row, col + 1, Country)
            worksheet.write(row, col + 2, ISO)
            worksheet.write(row, col + 3, Admin1)
            worksheet.write(row, col + 4, Admin2)
            worksheet.write(row, col + 5, Start)
            worksheet.write(row, col + 6, End)
            worksheet.write(row, col + 7, Affected)
            worksheet.write(row, col + 8, Assisted)
            worksheet.write(row, col + 9, Glide)
            worksheet.write(row, col + 10, OpNum)
            worksheet.write(row, col + 11, OpBud)
            worksheet.write(row, col + 12, Host)

        workbook.close() '''

    

# test = main("src/Backend/Integration/testfile.pdf")
path = "src/Backend/Integration/MDRRW014dfr.pdf" #edit
#test = main(path)
#file_num = 1 #edit
#print(test.final_extract)
#dict_parser(test.final_extract,path,file_num)
test_dict = {'Country': 'Rwanda', 'ISO': 'RWA', 'Admin1': [{'Location': 'Eastern Province', 'P-Code': '20RWA005'}, {'Location': 'the City of Kigali', 'P-Code': '20RWA001'}], 'Admin2': [{'Location': 'Flanders', 'P-Code': '20RWA004042'}, {'Location': 'Gatsibo district', 'P-Code': '20RWA005053'}, {'Location': 'Gatsibo District', 'P-Code': '20RWA005053'}, {'Location': 'Gatsibo d istrict \n©IFRC', 'P-Code': '20R053WA005053'}], 'Start': '11 July 2017', 'End': '01 September 2017', 'Affected': '675', 'Assisted': '811 households', 'Glide': 'ST-2017 -000035 -RWA', 'OpNum': 'MDRRW014', 'OpBud': 'CHF 49,122', 'Host': 'Rwanda Red Cross Society'}
dict_parser(test_dict,path)