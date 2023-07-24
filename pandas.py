# Mark Klingelhoefer
# Module 7
# 7/23/23
# M07 Lab: Case Study Part 1

import numpy as np
import pandas as pd

# Create NumPy array and dictionary
labels = ['a', 'b', 'c']

my_list = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a':10, 'b':20, 'c':30}

# Creates a pandas series with labels
pd.Series(my_list, index=labels)

# Functions sum, print, len
pd.Series([sum, print, len])
