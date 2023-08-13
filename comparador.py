import pandas as pd
import numpy as np

df1 = pd.read_excel('My_Team_HQ_2023.xlsx')
df2 = pd.read_excel('My_Team_HQ_2023.xlsx')

array1 = np.array(df1) # ===> Storing the data in an array will allow the equation below to show the differences.
array2 = np.array(df2)

df_CSV_1 = pd.DataFrame(array1, columns=["CRID", "1st Name", "Last Name", "PS"])
df_CSV_2 = pd.DataFrame(array2, columns=["CRID", "1st Name", "Last Name", "PS"])

df_CSV_1.index += 1 # ===> This resets the index to start at 1 not 0, helps with the output when trying to understand the differences.
df_CSV_2.index += 1

df_CSV_1.index += 1 # ===> This resets the index to start at 1 not 0, helps with the output when trying to understand the differences.
df_CSV_2.index += 1

print=(df_CSV_1.eq(df_CSV_2).to_string(index=True)) #===> This shows the differences between the two arrays.

df_CSV_1.eq(df_CSV_2).to_excel("tempp.xlsx")