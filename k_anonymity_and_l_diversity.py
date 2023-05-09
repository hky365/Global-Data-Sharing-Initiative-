#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv("<file_path_origin>")
# Define the quasi-identifier attributes
quasi_identifiers = ['age_in_cat', 'sex'] #Here we take "age_in_cat" and "sex" as examples, you can adapt it

# Define the sensitive attributes
sensitive_attributes = [
    'com_cardiovascular_disease', 'com_chronic_liver_disease', 'com_chronic_kidney_disease',
    'com_diabetes', 'com_hypertension', 'com_immunodeficiency', 'com_lung_disease',
    'com_malignancy', 'com_neurological_neuromuscular'
] #adapt it according to your dataset and outcome

def compute_l_diversity(df, quasi_identifiers, sensitive_attribute):
    # Group the dataset by quasi-identifiers
    grouped_df = df.groupby(quasi_identifiers)

    # Compute the l-diversity for each group
    l_diversities = []
    for _, group in grouped_df:
        l_diversity = len(group[sensitive_attribute].unique())
        l_diversities.append(l_diversity)

    # Calculate the minimum l-diversity across all groups
    min_l_diversity = min(l_diversities)
    return min_l_diversity

# Calculate the l-diversity for each sensitive attribute
l_diversity_results = {}
for sensitive_attribute in sensitive_attributes:
    min_l_diversity = compute_l_diversity(df, quasi_identifiers, sensitive_attribute)
    l_diversity_results[sensitive_attribute] = min_l_diversity

# Print the l-diversity results
for sensitive_attribute, min_l_diversity in l_diversity_results.items():
    print(f"Minimum l-diversity for {sensitive_attribute}: {min_l_diversity}")
    

def compute_k_anonymity(df, quasi_identifiers):
    # Group the dataset by quasi-identifiers
    grouped_df = df.groupby(quasi_identifiers)

    # Compute the size of each group
    group_sizes = []
    for _, group in grouped_df:
        group_size = len(group)
        group_sizes.append(group_size)

    # Calculate the minimum group size (k-anonymity) across all groups
    min_k_anonymity = min(group_sizes)
    return min_k_anonymity

# Calculate the k-anonymity
k_anonymity = compute_k_anonymity(df, quasi_identifiers)
print(f"Minimum k-anonymity: {k_anonymity}")

