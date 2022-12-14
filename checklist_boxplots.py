import pandas as pd
import numpy as np
import csv

# data = pd.read_csv('C:/Users\RAJARSHI SAHA\OneDrive/Desktop/VIT FALL SEM 21-22/DATA VIZ/PROJECT/train.csv')
mat_data = pd.read_csv('C:/Users/Mayukh/Downloads/superconduct/unique_m.csv')
mat_df=mat_data
alkali_list=[list(mat_df.columns)[2],list(mat_df.columns)[10],list(mat_df.columns)[18],list(mat_df.columns)[36],list(mat_df.columns)[54]]
alkaline_list=[list(mat_df.columns)[3],list(mat_df.columns)[11],list(mat_df.columns)[19],list(mat_df.columns)[37],list(mat_df.columns)[55]]
transition_list=(list(mat_df.columns)[20:29])+(list(mat_df.columns)[38:47])+(list(mat_df.columns)[71:79])
posttransition_list=list(mat_df.columns)[12:13]+list(mat_df.columns)[29:31]+list(mat_df.columns)[47:50]+list(mat_df.columns)[79:85]
lantha_list=list(mat_df.columns)[56:71]
metalloids_list=list(mat_df.columns)[4:5]+list(mat_df.columns)[13:14]+list(mat_df.columns)[31:33]+list(mat_df.columns)[50:52]
nonmetals_list=list(mat_df.columns)[0:1]+list(mat_df.columns)[5:9]+list(mat_df.columns)[14:17]+list(mat_df.columns)[33:35]+list(mat_df.columns)[52:53]
noble_list=[list(mat_df.columns)[1],list(mat_df.columns)[9],list(mat_df.columns)[17],list(mat_df.columns)[35],list(mat_df.columns)[53],list(mat_df.columns)[85]]
mat_df['alkali_metals']=mat_df[alkali_list].max(axis=1)
mat_df['alkaline_earth_metals']=mat_df[alkaline_list].max(axis=1)
mat_df['transition_metals']=mat_df[transition_list].max(axis=1)
mat_df['posttransition_metals']=mat_df[posttransition_list].max(axis=1)
mat_df['lanthanoid_metals']=mat_df[lantha_list].max(axis=1)
mat_df['metalloids']=mat_df[metalloids_list].max(axis=1)
mat_df['reactive_nonmetals']=mat_df[nonmetals_list].max(axis=1)
mat_df['noble_gases']=mat_df[noble_list].max(axis=1)

for i in range(0,21263):
    for j in alkali_list:
        if(mat_df.iloc[i,88]!=0):
            if(mat_df[j][i]==mat_df.iloc[i,88]):
                mat_df.iloc[i,88]=j
# print(mat_df.iloc[:,88])

for i in range(0,21263):
    for j in alkaline_list:
        if(mat_df.iloc[i,89]!=0):
            if(mat_df[j][i]==mat_df.iloc[i,89]):
                mat_df.iloc[i,89]=j
# print(mat_df.iloc[:,89])

for i in range(0,21263):
    for j in transition_list:
        if(mat_df.iloc[i,90]!=0):
            if(mat_df[j][i]==mat_df.iloc[i,90]):
                mat_df.iloc[i,90]=j
               
for i in range(0,21263):
    for j in posttransition_list:
        if(mat_df.iloc[i,91]!=0):
            if(mat_df[j][i]==mat_df.iloc[i,91]):                                                                        
                mat_df.iloc[i,91]=j
               
for i in range(0,21263):
    for j in lantha_list:
        if(mat_df.iloc[i,92]!=0):
            if(mat_df[j][i]==mat_df.iloc[i,92]):
                mat_df.iloc[i,92]=j
               
for i in range(0,21263):
    for j in metalloids_list:
        if(mat_df.iloc[i,93]!=0):
            if(mat_df[j][i]==mat_df.iloc[i,93]):
                mat_df.iloc[i,93]=j
               
for i in range(0,21263):
    for j in nonmetals_list:
        if(mat_df.iloc[i,94]!=0):
            if(mat_df[j][i]==mat_df.iloc[i,94]):
                mat_df.iloc[i,94]=j
mat_df['tc_quantile']=pd.qcut(mat_df['critical_temp'],q=5,labels=["very low critical temp(< 4 K)","low critical temp(< 12 K)","moderate critical temp(< 32 K)","high critical temp(< 74 K)","very high critical temp(< 185 K)"],precision=0)
print(mat_df.iloc[:,88:95])

with open('reduced_set_red_and_green.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(['name','class'])
    write.writerows(files) 