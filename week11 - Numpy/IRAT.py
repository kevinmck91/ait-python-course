import numpy as np

data = np.loadtxt("wine.csv" , delimiter=",", skiprows=1)

print(data.shape[0])
print(type(data))
print(data.shape[1])
print(data.size)
print(data.ndim)
print(data[4][2])
print(type(data[4][2]))

chlorides,density,pH,sulphates,alcohol,quality = data.transpose()

print(quality.ndim)
print(quality.max())
print(quality.min())
print(quality.mean())
print(np.median(quality))
print(np.corrcoef(quality,alcohol))
print(np.corrcoef(quality,density))
print(np.corrcoef(quality,chlorides))
print(np.corrcoef(quality,sulphates))