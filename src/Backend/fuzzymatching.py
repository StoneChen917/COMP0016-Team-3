
import numpy as np
import pandas as pd

def findEditDistance(str1, str2):
    # Initialize the zero matrix
    row_length = len(str1) + 1
    col_length = len(str2) + 1
    distance = np.zeros((row_length, col_length), dtype=int)

    # Populate matrix of zeros with the indices of each character of both strings
    for i in range(1, row_length):
        for k in range(1, col_length):
            distance[i][0] = i
            distance[0][k] = k

    # Writing loops to find the cost of deletion, addition and substitution
    for col in range(1, col_length):
        for row in range(1, row_length):
            if str1[row - 1] == str2[col - 1]:
                cost = 0  # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                cost = 1

            distance[row][col] = min(distance[row - 1][col] + 1,  # Cost of removal
                                     distance[row][col - 1] + 1,  # Cost of addition
                                     distance[row - 1][col - 1] + cost)  # Cost of substitution

    distance = distance[row][col]
    return distance


def presentInSpreadsheet(loc):
    df = pd.read_excel(r'D:\admin1_ISOcodes.xlsx')
    if loc in df['subdivision_name'].values:
        row_num = df[df['subdivision_name'] == loc].index.to_numpy()
        int_row_num = int(row_num[0])
        code = df.iat[int_row_num, 1]
        return code

    else:
        col_list = df['subdivision_name'].values.tolist()

        for i in col_list:
            if findEditDistance(i, loc) < 3:
                row_num = df[df['subdivision_name'] == i].index.to_numpy()
                int_row_num = int(row_num[0])
                code = df.iat[int_row_num, 1]
                return code

print(presentInSpreadsheet('Dubai'))