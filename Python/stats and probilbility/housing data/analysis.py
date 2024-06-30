import pandas as f
from pandas_profiling import ProfileReport
g=f.read_csv('data.csv')
# print(g)
P=ProfileReport(g,minimal=True)
P.to_file(output_file='housing.html')