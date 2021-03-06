# Use pandas method "read_csv" to read csv files
import pandas as pd
csv_path='owid-covid-data.csv'
file1=pd.read_csv(csv_path)
print(file1.head())

# Use pandas method "read_excel" to read csv files
import pandas as pd
excel_path='MusicData.xlsx'
file2=pd.read_excel(excel_path)
print(file2.head())

# Use pandas method "dataframe" to read dictionaries

songs={
"Album":["Thriller", "Back in Black", "Dark Side if the moon", "The Bodyguard", "Bat out of Hell"],
"Released_year": [1982, 1980, 1973, 1992, 1977],
"Length_minutes":[42,42,42,57,46]
}
import pandas as pd
file3=pd.DataFrame(songs)
print(file3)

#Subsetting the dataframes - Single column
print("This is a subset of Covid Data file ")
file1_subset=file1[["location","new_cases"]]
print(file1_subset.head())
