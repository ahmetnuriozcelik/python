import pandas as pd
covid_all=pd.read_csv("owid-covid-data.csv")
#Slices the file with the selected columns below
covid_sliced = covid_all[["location","new_cases_per_million","date"]]
#Slices the file with condition location=Canada
condition= covid_sliced['location']=="Canada" and covid_sliced[new_cases_per_million]>0
covid_canada=covid_sliced[condition]
#writes the file to a csv file
covid_canada.to_csv('covid-canada.csv')
