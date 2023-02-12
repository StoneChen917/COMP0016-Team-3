from sentence_transformers import SentenceTransformer, util
import numpy as np
from transformers.models.decision_transformer.modeling_decision_transformer import DecisionTransformerGPT2PreTrainedModel
import pandas as pd


class Cosine():
    
    def __init__(self, admin_0, loc_list):
        self.admin_0 = admin_0
        # list of dict of pcodes for admin 1 & locations
        self.p_code_1 = []
        self.p_code_2 = []
        self.ISO_code = self.getISOCode()
        self.loc_list = loc_list


    
    def find_cosine_score(self,word1, word2):
        model = SentenceTransformer('stsb-roberta-large', device='cpu')
        # encode sentences to get their embeddings
        embedding1 = model.encode(word1, convert_to_tensor=True)
        embedding2 = model.encode(word2, convert_to_tensor=True)
        # compute similarity scores of two embeddings
        cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)

        return (cosine_scores.item())


    def getISOCode(self):
        bestCosSimScore = 0
        row_num = 0
        int_row_num = 0
        loc = self.admin_0

        df0 = pd.read_excel('src/Backend/Integration/admin0_codes.xlsx')
        # filter by first letter of country
        df0_filtered = df0[(df0['attributes_iso3'] != 'AAA') & (df0['attributes.gis_name'].str[0] == loc[0])]

        if loc in df0_filtered['attributes.gis_name'].values:
            row_num = df0[df0['attributes.gis_name'] == loc].index.to_numpy()
            int_row_num = int(row_num[0])
            code = df0.iat[int_row_num, 3]
            return (code)

        else:
            bestCosSimScore = 0
            for i in df0_filtered['attributes.gis_name'].values:
                score = self.find_cosine_score(loc, i)
                if score > bestCosSimScore:
                    bestCosSimScore = score
                    row_num = df0[df0['attributes.gis_name'] == i].index.to_numpy()
                    int_row_num = int(row_num[0])
                    code = df0.iat[int_row_num, 2]
            
            return (str(code))
    
    def find_p_code(self, loc):
  
        bestCosSimScore = 0
        row_num = 0
        int_row_num = 0

        df1 = pd.read_excel('src/Backend/Integration/admin1_codes.xlsx')
        df2 = pd.read_excel('src/Backend/Integration/admin2_codes.xlsx')

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

        df1_filtered = df1[(df1.attributes_iso3 == self.ISO_code) & (df1['attributes.gis_name'].str[0] == loc[0])]
        df2_filtered = df2[(df2.attributes_iso3 == self.ISO_code) & (df2['attributes.gis_name'].str[0] == loc[0])]

        bestCosSimScore1 = 0
        for i in df1_filtered['attributes.gis_name'].values:
            score1 = self.find_cosine_score(loc, i)
            if score1 > bestCosSimScore1:
                bestCosSimScore1 = score1
                row_num = df1[df1['attributes.gis_name'] == i].index.to_numpy()
                int_row_num = int(row_num[0])
                code1 = df1.iat[int_row_num, 3]

        bestCosSimScore2 = 0
        for i in df2_filtered['attributes.gis_name'].values:
            score2 = self.find_cosine_score(loc, i)
            if score2 > bestCosSimScore2:
                bestCosSimScore2 = score2
                row_num = df2[df2['attributes.gis_name'] == i].index.to_numpy()
                int_row_num = int(row_num[0])
                code2 = df2.iat[int_row_num, 3]    

        if bestCosSimScore1 > bestCosSimScore2:
            return (1,code1)
        return (2,code2)
    
    def loop_p_codes(self):
        for loc in self.loc_list:
            tag = self.find_p_code(loc)[0]
            p_code = self.find_p_code(loc)[1]
            dict = {"Location":loc, "P-Code":p_code}
            if tag == 1:
                self.p_code_1.append(dict)
            else:
                self.p_code_2.append(dict)

    
                
# test = Cosine("United States of America", ["West Virginia", "Vermont"])
# test.loop_p_codes()
# print(test.p_code_1)
# print(test.p_code_2)