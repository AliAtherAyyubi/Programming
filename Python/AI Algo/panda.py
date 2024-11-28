

import pandas as pd

# file=pd.read_csv('GOOGLE.csv')
file=pd.read_csv('GOOGLE.csv',names=['Date','Open'])
# file=pd.read_csv('info.txt')

print(file)