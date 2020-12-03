import numpy as np
from random import randint

data = np.loadtxt("professional.csv", encoding='utf8', usecols=(0, 3, 4, 6), delimiter=",", skiprows=1)

Idx,year,month,quarter = data.transpose()

frequency_dict = {}

for number in quarter:

    if number not in frequency_dict:
        frequency_dict[number] = 1
    else:
        frequency_dict[number] += 1

sorted_dict = dict(sorted(frequency_dict.items()))

print(sorted_dict)