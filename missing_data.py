# Mark Klingelhoefer
# Module 7
# 7/23/23
# M07 Lab: Case Study Part 3

import numpy as np
import pandas as pd

# Returns NaN
np.nan


df = pd.DataFrame(np.array([[1, 5, 1],[2, np.nan, 2],[np.nan, np.nan, 3]]))
df.columns = ['A', 'B', 'C']
df

# Removes any rows with NaN value
df.dropna()
# Removes columns that are missing values
df.dropna(axis=1)

# Fills every missing value in the dataframe
df.fillna('?')

# Fills missing values with average value
df['A'].fillna(df['A'].mean())
