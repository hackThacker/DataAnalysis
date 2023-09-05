import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('customers-100000.csv')

#generate a report
profile = ProfileReport(df)
profile.to_file(output_file="customers.html")

