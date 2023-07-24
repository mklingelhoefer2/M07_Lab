# Mark Klingelhoefer
# Module 7
# 7/23/23
# M07 Lab: Case Study Part 7

import numpy as np
import pandas as pd

leftDataFrame = pd.DataFrame({  'A': ['A0', 'A1', 'A2', 'A3'],

                                'B': ['B0', 'B1', 'B2', 'B3']},

                                index =['K0', 'K1', 'K2', 'K3'])

   

rightDataFrame = pd.DataFrame({ 'C': ['C0', 'C1', 'C2', 'C3'],

                                'D': ['D0', 'D1', 'D2', 'D3']},

                                index = ['K0', 'K1', 'K2', 'K3'])  

# Joins dataframes
# Difference between this and merge is that the keys that are combined are in the index instead of contained within a column
leftDataFrame.join(rightDataFrame)

# Other common operations

df = pd.DataFrame({'col1':['A','B','C','D'],

                   'col2':[2,7,3,7],

                   'col3':['fgh','rty','asd','qwe']})

# Finds unique values in a column
df['col2'].unique()
# Returns number of unique values in column
df['col2'].nunique()

# Count number of time each value occurs
df['col2'].value_counts()

def exponentify(x):

    return x**x
# Applies exponentify method to each element
df['col2'].apply(exponentify)

# Sorts 2nd column
df.sort_values('col2')
