# Mark Klingelhoefer
# Module 7
# 7/23/23
# M07 Lab: Case Study Part 6

import numpy as np
import pandas as pd

leftDataFrame = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],

                     'A': ['A0', 'A1', 'A2', 'A3'],

                     'B': ['B0', 'B1', 'B2', 'B3']})

   

rightDataFrame = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],

                          'C': ['C0', 'C1', 'C2', 'C3'],

                          'D': ['D0', 'D1', 'D2', 'D3']}) 

# Merges dataframe
pd.merge(leftDataFrame, rightDataFrame, how='inner', on='key')