import numpy as np
import pandas as pd
import time
from sentence_transformers import SentenceTransformer, util
import numpy as np
model = SentenceTransformer('stsb-roberta-large', device='cpu')
from fuzzywuzzy import fuzz
from transformers.models.decision_transformer.modeling_decision_transformer import DecisionTransformerGPT2PreTrainedModel

# st = time.time()

# def findEditDistance(str1, str2):
#     # Initialize the zero matrix
#     row_length = len(str1) + 1
#     col_length = len(str2) + 1
#     distance = np.zeros((row_length, col_length), dtype=int)

#     # Populate matrix of zeros with the indices of each character of both strings
#     for i in range(1, row_length):
#         for k in range(1, col_length):
#             distance[i][0] = i
#             distance[0][k] = k

#     # Writing loops to find the cost of deletion, addition and substitution
#     for col in range(1, col_length):
#         for row in range(1, row_length):
#             if str1[row - 1] == str2[col - 1]:
#                 cost = 0  # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
#             else:
#                 cost = 1

#             distance[row][col] = min(distance[row - 1][col] + 1,  # Cost of removal
#                                      distance[row][col - 1] + 1,  # Cost of addition
#                                      distance[row - 1][col - 1] + cost)  # Cost of substitution

#     distance = distance[row][col]
#     return distance

# def mapToISOCodesUsingEditDistance(loc, admin0Code):
#   row_num = 0
#   int_row_num = 0

#   df1 = pd.read_excel(r"D:\admin1_codes.xlsx")
#   df2 = pd.read_excel(r"D:\admin2_codes.xlsx")

#   if loc in df1['attributes.gis_name'].values:
#     row_num = df1[df1['attributes.gis_name'] == loc].index.to_numpy()
#     int_row_num = int(row_num[0])
#     code = df1.iat[int_row_num, 3]
#     return code

#   elif loc in df2['attributes.gis_name'].values:
#     row_num = df2[df2['attributes.gis_name'] == loc].index.to_numpy()
#     int_row_num = int(row_num[0])
#     code = df2.iat[int_row_num, 3]
#     return code

#   else:
#     df1_filtered = df1[(df1.attributes_iso3 == admin0Code)]
#     df2_filtered = df2[(df2.attributes_iso3 == admin0Code)]

#     bestEditDist1 = 100
#     for i in df1_filtered['attributes.gis_name'].values:
#       score1 = findEditDistance(loc, i)
#       if score1 < bestEditDist1:
#         bestEditDist1 = score1
#         row_num = df1[df1['attributes.gis_name'] == i].index.to_numpy()
#         int_row_num = int(row_num[0])
#         code1 = df1.iat[int_row_num, 3]

#     bestEditDist2 = 100
#     for i in df2_filtered['attributes.gis_name'].values:
#       score2 = findEditDistance(loc, i)
#       if score2 < bestEditDist2:
#         bestEditDist2 = score2
#         row_num = df2[df2['attributes.gis_name'] == i].index.to_numpy()
#         int_row_num = int(row_num[0])
#         code2 = df2.iat[int_row_num, 3]

#     if bestEditDist1 == 100 and bestEditDist2 == 100:
#       return None
#     elif bestEditDist1 == bestEditDist2:
#       return code1
#     elif bestEditDist2 < bestEditDist1:
#       return code2
#     elif bestEditDist1 < bestEditDist2:
#       return code1

# locations = []
# countryCodes = []
# results = []
# def gettingResults():
#   df = pd.read_excel(r"D:\testData.xlsx")

#   for loc in df['Location'].values:
#     locations.append(loc)

#   for code in df['CountryCode'].values:
#     countryCodes.append(code)

#   for i in range(len(locations)):
#     print(mapToISOCodesUsingEditDistance(locations[i], countryCodes[i]))
#     results.append(mapToISOCodesUsingEditDistance(locations[i], countryCodes[i]))

# gettingResults()
# print(results)

# et = time.time()
# elapsed_time = et - st
# print('Execution time:', elapsed_time, 'seconds')

# print(findEditDistance('Guangzhou', 'Guangzhu'))
# print(findEditDistance('Guangzhou', 'Gansu'))
# print(mapToISOCodesUsingEditDistance('Guangzhu', 'CHN'))


# df = pd.read_excel(r"D:\testData.xlsx")
# correct = []
# results = ['21CHN017004', '20SRB001024', '21CHN006004', '20USA001061', '20FRA013003', '20SAU013001', '20USA036', '20YEM011008', '20YEM023', '20YEM028004', '20YEM017', '20GIN008005', '20TZA016', '21GHA010', '20GIN002', '20KEN047', '21MKD007005', '20MNE007', '20MNE013', '21MKD008009', '20HUN005', '20MNE010', '21MKD005', '20LKA001001', '20LKA002001', '20LKA002002', '20LKA001003', '20LKA003003', '20LKA005001', '20KEN010', '20KHM012006', '22ETH003010', '20KEN010045', '20KHM003', '20ZMB005005', '20ZWE011005', '20ZAF003001', '20KHM007', '20BOL003', '20KHM012']
# for i in df['Code'].values:
#   correct.append(i)

# total = len(correct)
# count = 0
# output = []

# st2 = time.time()
# def FindCosSim(word1, word2):
#   # encode sentences to get their embeddings
#   embedding1 = model.encode(word1, convert_to_tensor=True)
#   embedding2 = model.encode(word2, convert_to_tensor=True)
#   # compute similarity scores of two embeddings
#   cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)

#   return cosine_scores.item()


# def mapToISOCodesUsingCosSim(loc, admin0Code):
#   bestCosSimScore = 0
#   row_num = 0
#   int_row_num = 0

#   df1 = pd.read_excel(r"D:\admin1_codes.xlsx")
#   df2 = pd.read_excel(r"D:\admin2_codes.xlsx")

#   if loc in df1['attributes.gis_name'].values:
#     row_num = df1[df1['attributes.gis_name'] == loc].index.to_numpy()
#     int_row_num = int(row_num[0])
#     code = df1.iat[int_row_num, 3]
#     return code

#   elif loc in df2['attributes.gis_name'].values:
#     row_num = df2[df2['attributes.gis_name'] == loc].index.to_numpy()
#     int_row_num = int(row_num[0])
#     code = df2.iat[int_row_num, 3]
#     return code

#   else:
#     df1_filtered = df1[(df1.attributes_iso3 == admin0Code) & (df1['attributes.gis_name'].str[0] == loc[0])]
#     df2_filtered = df2[(df2.attributes_iso3 == admin0Code) & (df2['attributes.gis_name'].str[0] == loc[0])]

#     bestCosSimScore1 = 0
#     for i in df1_filtered['attributes.gis_name'].values:
#       score1 = FindCosSim(loc, i)
#       if score1 > bestCosSimScore1:
#         bestCosSimScore1 = score1
#         row_num = df1[df1['attributes.gis_name'] == i].index.to_numpy()
#         int_row_num = int(row_num[0])
#         code1 = df1.iat[int_row_num, 3]

#     bestCosSimScore2 = 0
#     for i in df2_filtered['attributes.gis_name'].values:
#       score2 = FindCosSim(loc, i)
#       if score2 > bestCosSimScore2:
#         bestCosSimScore2 = score2
#         row_num = df2[df2['attributes.gis_name'] == i].index.to_numpy()
#         int_row_num = int(row_num[0])
#         code2 = df2.iat[int_row_num, 3]   

#     if bestCosSimScore1 == 0 and bestCosSimScore2 == 0:
#       return None
#     elif bestCosSimScore1 == bestCosSimScore2:
#       return code1
#     elif bestCosSimScore2 > bestCosSimScore1:
#       return code2
#     elif bestCosSimScore1 > bestCosSimScore2:
#       return code1

# locations = []
# countryCodes = []
# results2 = []
# def gettingResultsCS():
#   df = pd.read_excel(r"D:\testData.xlsx")

#   for loc in df['Location'].values:
#     locations.append(loc)

#   for code in df['CountryCode'].values:
#     countryCodes.append(code)

#   for i in range(len(locations)):
#     print(mapToISOCodesUsingCosSim(locations[i], countryCodes[i]))
#     results2.append(mapToISOCodesUsingCosSim(locations[i], countryCodes[i]))


# gettingResultsCS()
# print(results2)

# et2 = time.time()
# elapsed_time2 = et2 - st2
# print('Execution time:', elapsed_time2, 'seconds')


st3 = time.time()
def checkFuzzyRatio(word1, word2):
  return fuzz.ratio(word1, word2)

for i in range(10):
  # still takes in location and admin 0 code
  def mapToISOCodesUsingFuzzyMatching(loc, admin0Code):
    row_num = 0
    int_row_num = 0

    df1 = pd.read_excel(r"D:\admin1_codes.xlsx")
    df2 = pd.read_excel(r"D:\admin2_codes.xlsx")

    # find exact match in admin 1
    if loc in df1['attributes.gis_name'].values:
      row_num = df1[df1['attributes.gis_name'] == loc].index.to_numpy()
      int_row_num = int(row_num[0])
      code = df1.iat[int_row_num, 3]
      return code

    # find exact match in admin 2
    elif loc in df2['attributes.gis_name'].values:
      row_num = df2[df2['attributes.gis_name'] == loc].index.to_numpy()
      int_row_num = int(row_num[0])
      code = df2.iat[int_row_num, 3]
      return code

    # find best match in 1 & 2
    else:
      df1_filtered = df1[(df1.attributes_iso3 == admin0Code)]
      df2_filtered = df2[(df2.attributes_iso3 == admin0Code)]


      bestFuzzyRatio1 = 0
      for i in df1_filtered['attributes.gis_name'].values:
        score1 = checkFuzzyRatio(loc, i)
        if score1 > bestFuzzyRatio1:
          bestFuzzyRatio1 = score1
          row_num = df1[df1['attributes.gis_name'] == i].index.to_numpy()
          int_row_num = int(row_num[0])
          code1 = df1.iat[int_row_num, 3]

      bestFuzzyRatio2 = 0
      for i in df2_filtered['attributes.gis_name'].values:
        score2 = checkFuzzyRatio(loc, i)
        if score2 > bestFuzzyRatio2:
          bestFuzzyRatio2 = score2
          row_num = df2[df2['attributes.gis_name'] == i].index.to_numpy()
          int_row_num = int(row_num[0])
          code2 = df2.iat[int_row_num, 3] 

      if bestFuzzyRatio1 == 0 and bestFuzzyRatio2 == 0:
        return None
      elif bestFuzzyRatio1 == bestFuzzyRatio2:
        return code1
      elif bestFuzzyRatio2 > bestFuzzyRatio1:
        return code2
      elif bestFuzzyRatio1 > bestFuzzyRatio2:
        return code1

  locations = []
  countryCodes = []
  results3 = []

  def gettingResultsFM():
    df = pd.read_excel(r"D:\testData.xlsx")

    for loc in df['Location'].values:
      locations.append(loc)

    for code in df['CountryCode'].values:
      countryCodes.append(code)

    for i in range(len(locations)):
      print(mapToISOCodesUsingFuzzyMatching(locations[i], countryCodes[i]))
      results3.append(mapToISOCodesUsingFuzzyMatching(locations[i], countryCodes[i]))


  gettingResultsFM()
  print(results3)

et3 = time.time()
elapsed_time3 = (et3 - st3)/10
print('Execution time:', elapsed_time3, 'seconds')