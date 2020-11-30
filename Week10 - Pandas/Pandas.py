import pandas as pd

# Read in every column
# df = pd.read_csv("avocado.csv")
df = pd.read_csv("avocado.csv", usecols=['Date', 'AveragePrice', 'type', 'region', '4770', 'Total Bags'])

# so we dont have to cal DF each time
average_prices_col = df.get("AveragePrice")


print("\n 1. Number of values in the file  ************************************************************************\n")

print(df.size)

print("\n 2. Top few lines of a file   ************************************************************************\n")

print(df.head())

print("\n 3. Show the list of columns   ************************************************************************\n")

print(df.columns)

print("\n 4. Count the values in each column ************************************************************************\n")

print(df.count())

print("\n 5. Get a statistics of the numerical colums ************************************************************************\n")

print(df.describe())

print("\n 6. Access an individual column ************************************************************************\n")

# Get a column as a series (that looks and acts like a dictionary)
print(type(average_prices_col))
print('max', average_prices_col.max())
print('min', average_prices_col.min())
print('count', average_prices_col.count())
print('median', average_prices_col.median())
print('ID of row with the max average price', average_prices_col.idxmax())


print("\n 7. print a row based on ID ************************************************************************\n")

# Get the row ID of the max value
max_value = average_prices_col.max()
row_id_of_max_value = average_prices_col.idxmax()

print(df.loc[row_id_of_max_value])


print("\n 8. Correlation between two columns ************************************************************************\n")

print(df.get('Total Bags').corr(df.get('4770')))


print("\n 9. Getting ratio between columns ************************************************************************\n")

ratios = df.get('Total Bags') / df.get('4770')
print(ratios)


print("\n 10. Check a specific set of values ************************************************************************\n")

check = df.get('AveragePrice') > 3
print(check)


print("\n 11. Create new list by filtering values  ************************************************************************\n")


filtered_series = df.AveragePrice[df.AveragePrice > 3]
print(filtered_series)


print("\n 12. get all the unique values in a column  ************************************************************************\n")

print(df.type.unique())


print("\n 13. Group data by type  ************************************************************************\n")

# Get the types and output the count for each type
print(df.groupby('type').size() , "\n")

# Get the types and output the averages for each type
print(df.groupby('type').mean() , "\n")


print("\n 13. plotting  ************************************************************************\n")

# Can only really be used in the the compiler

print(df.type.hist())