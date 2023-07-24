# Mark Klingelhoefer
# Module 7
# 7/23/23
# M07 Lab: Case Study Part 4

import numpy as np
import pandas as pd

df = pd.DataFrame([ ['Google', 'Sam', 200],

                    ['Google', 'Charlie', 120],

                    ['Salesforce','Ralph', 125],

                    ['Salesforce','Emily', 250],

                    ['Adobe','Rosalynn', 150],

                    ['Adobe','Chelsea', 500]])
df.columns = ['Organization', 'Salesperson Name', 'Sales']
df

# Groups by organization
df.groupby('Organization')

# The mean (or average) of the sales column
df.groupby('Organization').mean()
# The sum of the sales column
df.groupby('Organization').sum()
# The standard deviation of the sales column
df.groupby('Organization').std()
# Counts the number of observations
df.groupby('Organization').count()
# Returns the maximum value
df.groupby('Organization').max()
# Returns the minimum value
df.groupby('Organization').min()
# Returns a table of information, such as mean, std, min, etc
df.groupby('Organization').describe()