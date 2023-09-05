import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('customers-100000.csv') # enter the files name which you want to genreate a report form

#generate a report
profile = ProfileReport(df)
profile.to_file(output_file="customers.html")

