from sentence_transformers import SentenceTransformer, util
import numpy as np
from transformers.models.decision_transformer.modeling_decision_transformer import DecisionTransformerGPT2PreTrainedModel
import pandas as pd
import numpy as np
import pandas as pd
import time
from sentence_transformers import SentenceTransformer, util
import numpy as np
model = SentenceTransformer('stsb-roberta-large', device='cpu')
from fuzzywuzzy import fuzz
from transformers.models.decision_transformer.modeling_decision_transformer import DecisionTransformerGPT2PreTrainedModel


class codeMatch():
    """Finds ISO code for Admin 0 locations and P-codes of Admin 1 & 2 locations
    methods getISOCode() and loop_p_codes(self) """
    def __init__(self, admin_0, loc_list):
        self.admin_0 = admin_0
        # list of dict of pcodes for admin 1 & locations
        self.loc_list = loc_list
        self.ISO_code = self.getISOCode()
        self.p_code_1 = []
        self.p_code_2 = []
        
        
    def find_fuzz_ratio(self,word1, word2):
        return fuzz.ratio(word1, word2)


    def getISOCode(self):
        row_num = 0
        int_row_num = 0
        loc = self.admin_0

        df0 = pd.read_excel('src/Backend/Integration/admin0_codes.xlsx')
        # filter by first letter of country
        df0_filtered = df0[(df0['attributes_iso3'] != 'AAA') & (df0['attributes.gis_name'].str[0] == loc[0])]

        # if exact match found
        if loc in df0_filtered['attributes.gis_name'].values:
            row_num = df0[df0['attributes.gis_name'] == loc].index.to_numpy()
            int_row_num = int(row_num[0])
            code = df0.iat[int_row_num, 3]
            return (code)

        # otherwise find best match
        else:
            best_fuzz_ratio = 0
            for i in df0_filtered['attributes.gis_name'].values:
                score = self.find_fuzz_ratio(loc, i)
                if score > best_fuzz_ratio:
                    best_fuzz_ratio = score
                    row_num = df0[df0['attributes.gis_name'] == i].index.to_numpy()
                    int_row_num = int(row_num[0])
                    code = df0.iat[int_row_num, 2]
            
            return (str(code))
    
    def find_p_code(self, loc):
  
        best_fuzz_ratio = 0
        row_num = 0
        int_row_num = 0

        df1 = pd.read_excel('src/Backend/Integration/admin1_codes.xlsx')
        df2 = pd.read_excel('src/Backend/Integration/admin2_codes.xlsx')

        # if exact match is found
        if loc in df1['attributes.gis_name'].values:
            row_num = df1[df1['attributes.gis_name'] == loc].index.to_numpy()
            int_row_num = int(row_num[0])
            code = df1.iat[int_row_num, 3]
            return (1,code)

        elif loc in df2['attributes.gis_name'].values:
            row_num = df2[df2['attributes.gis_name'] == loc].index.to_numpy()
            int_row_num = int(row_num[0])
            code = df2.iat[int_row_num, 3]
            return (2,code)

        # find best match in 1 & 2
        
        df1_filtered = df1[(df1.attributes_iso3 == self.ISO_code)]
        df2_filtered = df2[(df2.attributes_iso3 == self.ISO_code)]

        code1 = "None"
        code2 = "None"
        best_fuzz_ratio1 = 0
        for i in df1_filtered['attributes.gis_name'].values:
            score1 = self.find_fuzz_ratio(loc, i)
            if score1 > best_fuzz_ratio1:
                best_fuzz_ratio1 = score1
                row_num = df1[df1['attributes.gis_name'] == i].index.to_numpy()
                int_row_num = int(row_num[0])
                code1 = df1.iat[int_row_num, 3]

        best_fuzz_ratio2 = 0
        for i in df2_filtered['attributes.gis_name'].values:
            score2 = self.find_fuzz_ratio(loc, i)
            if score2 > best_fuzz_ratio2:
                best_fuzz_ratio2 = score2
                row_num = df2[df2['attributes.gis_name'] == i].index.to_numpy()
                int_row_num = int(row_num[0])
                code2 = df2.iat[int_row_num, 3]   

        if best_fuzz_ratio1 == 0 and best_fuzz_ratio2 == 0:
            return (0,"None")
        elif best_fuzz_ratio1 == best_fuzz_ratio2:
            return (1,code1)
        elif best_fuzz_ratio2 > best_fuzz_ratio1:
            return (2,code2)
        else:
            return (1,code1)


    
    def loop_p_codes(self):
        for loc in self.loc_list:
            tag = self.find_p_code(loc)[0]
            p_code = self.find_p_code(loc)[1]
            dict = {"Location":loc, "P-Code":p_code}
            if tag == 1:
                self.p_code_1.append(dict)
            if tag == 2:
                self.p_code_2.append(dict)
                

