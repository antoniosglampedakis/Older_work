import pandas as pd
pd.set_option('display.max_columns', None)


xls = pd.ExcelFile('TBWA_CL.xlsx')
df1 = pd.read_excel(xls, '2019 TBWA Entries')
df2 = pd.read_excel(xls, 'TBWA L3Y Companies')