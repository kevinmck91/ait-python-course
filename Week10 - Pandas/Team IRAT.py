# A00279670 - Movie_Ratings.csv

import pandas as pd

df = pd.read_csv("Movie_Ratings.csv")

print("\n Values = ", df.size)
print("\n Columns = ", len(df.columns))
print("\n Rows = ", len(df))
print("\n Headings = ", df.columns)

df = df.sort_values('imdb_score')
print("\n First 5 rows = ", df.head())


gross = df.get("gross")
print(type(gross))
print('\n max', gross.max())
print('\n min', gross.min())
print('\n count', gross.count())
print('\n median', gross.median())
print('\n ID of row with the max gross', gross.idxmax())
print('\n ID of row with the min gross', gross.idxmin())
print('\n correlation', print(df.get('gross').corr(df.get('imdb_score'))))
