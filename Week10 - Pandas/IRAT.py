import pandas as pd

# Read in every column
df = pd.read_csv("airline.csv")
df2 = pd.read_csv("airline.csv", usecols=['UniqueCarrier', 'FlightNum', 'ActualElapsedTime', 'CRSElapsedTime'])
df3 = pd.read_csv("airline.csv", usecols=list(range(10)))

# so we don't have to cal DF each time
print("\n 1 **************** \n")
print(df.size)

print("\n 2 **************** \n")
print(df2.size)

print("\n 3 **************** \n")
print(df3.size)

print("\n 4 **************** \n")
print(type(df))

print("\n 5 **************** \n")
print(df.count())

print("\n 6 **************** \n")
print("head", df.head)

print("\n 7 **************** \n")
print("Describe" , df.describe())

print("\n 8 **************** \n")
delay = df.DepDelay[df.DepDelay >= 0]
print(delay.size)

print("\n 9 **************** \n")
# Get the row ID of the max value
max_value = delay.max()
row_id_of_max_value = delay.idxmax()
print(row_id_of_max_value)

print("\n 10 **************** \n")
print(df.loc[row_id_of_max_value])


print("\n 11 **************** \n")
corr = df.ActualElapsedTime.corr(df.CRSElapsedTime)
print(corr)

print("\n 12 **************** \n")
print(df.groupby('UniqueCarrier').size())