# Mark Klingelhoefer
# Module 7
# 7/23/23
# M07 Lab: Case Study Part 2

import numpy as np
import pandas as pd

# Create rows and columns
rows = ['X','Y','Z']
cols = ['A', 'B', 'C', 'D', 'E']

# NumPy array that holds the data contained within the cells of the dataframe
data = np.round(np.random.randn(3,5),2)

# Creates dataframe
pd.DataFrame(data, rows, cols)

df = pd.DataFrame(data, rows, cols)

# Calling index from data frame
df['A']
df['E']

# Another way to call index from data frame
columnsIWant = ['A', 'E']
df[columnsIWant]

# Edits dataframe
df['A + B'] = df['A'] + df['B']
# New dataframe
df 

# Removes column from dataframe, but does not actually modify dataframe itself
df.drop('A + B', axis = 1)

# Removes column and modifies database itself
df = df.drop('A + B', axis=1)
df

# Drops row Z
df.drop('Z')

# Accesses row by its label
df.loc['X']
# Can also be accessed from their index using iloc
df.iloc[0]

# Gives amount of rows and columns in dataframe
df.shape

# Slices dataframe
df[['A', 'B']].loc[['X', 'Y']]

# Prints true or false for each column
df['C'] < 1

# Returns dataframe with combined conditionals
df[(df['C'] > 0) & (df['A']> 0)]

# Resets index to default
df.reset_index()
# Adds values of A into dataframe
df.set_index('A')

# Assigns new values to columns
df.columns = [1, 2, 3, 4, 5]
df