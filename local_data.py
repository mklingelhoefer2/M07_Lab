# Mark Klingelhoefer
# Module 7
# 7/23/23
# M07 Lab: Case Study Part 8

import numpy as np
import pandas as pd

pd.read_csv('stock_prices.csv')

# Data frame with value of csv
new_data_frame = pd.read_csv('stock_prices.csv')

# Creates dataframe and fills 3 columns and 50 rows with random data
df = pd.DataFrame(np.random.randn(50,3))

# Save new dataframe to csv
df.to_csv('my_new_csv.csv')

# Removes blank index column
new_data_frame.to_csv('my_new_csv.csv', index = False)

# Imports json file as a dataframe
json_data_frame = pd.read_json('stock_prices.json')

# Exports dataframe to new json file
df.to_json('my_new_json.json')

# Imports excel file as a dataframe
new_data_frame = pd.read_excel('stock_prices.xlsx')

# Imports excel sheet to dataframe
new_data_frame.to_excel('stock_prices.xlsx', sheet_name='Sheet2')

# Export xlsx file
df.to_excel('my_new_excel_file.xlsx')

# Exports xlsx file to new file
df.to_excel('my_new_excel_file.xlsx', sheet_name='My New Sheet!')

# Imports remote csv
pd.read_csv('https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv')
# Imports remote json
pd.read_json('https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.json')
# Imports remote excel
pd.read_excel('https://github.com/nicholasmccullum/advanced-python/blob/master/stock_prices/stock_prices.xlsx?raw=true')
