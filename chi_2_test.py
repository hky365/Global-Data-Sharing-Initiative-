#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


def compare_variables_updated_for_paper(df_original, df_anonymized, variables):
    print("Length of anonymized dataframe is: ", len(df_anonymized))
    print("Length of original dataframe is: ", len(df_original))
    for variable in variables:
        # check if variable exists in both datasets
        if variable in df_original.columns and variable in df_anonymized.columns:
            #get categories of variable in anonymized dataset
            categories = df_anonymized[variable].unique()
            #select only the rows with categories present in anonymized dataset
            df_original_var = df_original.loc[df_original[variable].isin(categories), [variable]]
            #calculate Cramer's V
            table = pd.crosstab(df_original_var[variable], df_anonymized[variable])
            n = table.sum().sum()
            colsum = table.sum(axis=0)
            rowsum = table.sum(axis=1)
            expected = np.outer(colsum, rowsum) / n
            chi2 = ((table - expected)**2 / expected).values.sum()
            cramerV = np.sqrt(chi2 / (n * (min(table.shape) - 1)))
            
            dof = (table.shape[0]-1)*(table.shape[1]-1)
            chi2, p = chisquare(f_obs=df_original_var[variable].value_counts(normalize=True), 
                                f_exp=df_anonymized[variable].value_counts(normalize=True))
            
            effect_size = np.sqrt(chi2/n)
            
            print()
            print("---------------------------------------------------------------------------------------------")
            print("Value counts of "+ variable + " in anonymized dataset")
            print()
            print(df_anonymized[variable].value_counts(dropna=False))
            print()
            print()
            print("---------------------------------------------------------------------------------------------")
            print("Value counts of "+ variable + " in original dataset")
            print()
            print(df_original[variable].value_counts(dropna=False))
            print()
            print(f'Cramer V for {variable}: {cramerV}')
            print(f'Chi-Squared test for {variable}, p-value: {p}, degrees of freedom: {dof}')
            print(f'test statistic for {variable}: {chi2}')
            print(f'Effect size for {variable}: {effect_size}')
            
            #barplot
            original_counts = df_original_var[variable].value_counts()
            anonymized_counts = df_anonymized[variable].value_counts()
            data = pd.concat([original_counts, anonymized_counts], axis=1)
            data.columns = ['original', 'anonymized']
            data.plot(kind='bar', stacked=False)
            plt.show()
        else:
            print(f"{variable} not found in both datasets, skipping")

compare_variables_updated_for_paper(df_orig_final, df_anon_final, ['secret_name','age_in_cat', 'sex', 'covid19_diagnosis', 'ms_type2', 'bmi_in_cat2', 
                         'covid19_ventilation', 'com_cardiovascular_disease', 
        'com_chronic_liver_disease','com_chronic_kidney_disease', 'com_diabetes',  
       'com_hypertension', 'com_immunodeficiency', 'com_lung_disease', 
       'com_malignancy','com_neurological_neuromuscular']) # original dataframe, anonymised(subset) of original dataframe with variables of interest

