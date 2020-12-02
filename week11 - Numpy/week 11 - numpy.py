
import numpy as np
from random import randint


print("\n 1. Create a 1D array  ************************************************************************\n")

a1 = np.array([1,2,3,4,5,6])    # only takes one argument, a list or tuple
print('a1 = ' , a1)
print('len(a1) = ' , len(a1))
print('a1.shape = ' , a1.shape)
print('\n')

a2 = np.arange(1,8)
print('a2 = ' , a1)
print('len(a2) = ' , len(a2))
print('\n')

numbers = [randint(1,6) for i in range(5)]      # any list can be turned into an array
a3 = np.array(numbers)
print('a3 = ' , a3)
print('\n')

a4 = np.random.randint(1,6,9)       # Generate 9 numbers between 1 and 5
print('a4 = ' , a4)


print("\n 1. Create a N x M array  ************************************************************************\n")

a5 = np.random.randint(1,6,size=(2,10))       # Generate 9 numbers between 1 and 5
print('a5 = ' , a5)
print('a5.shape = ' , a5.shape)
print('\n')

a6 = np.array([(0,1,2,3,4,5),(10,20,30,40,50,60)])       # Generate 9 numbers between 1 and 5
print('a6 = ' , a6)
print('a6.shape = ' , a6.shape)           # 2 rows 56 columns - Axis0 refers to the ros
print('a6.shape[0] = ' , a6.shape[0])     # number of rows
print('len(a6)' , len(a6))                # number of rows
print('a6.shape[1] = ' , a6.shape[1])     # number of columns
print('a6.size = ' , a6.size)             # number of Rows x Columns




print('\n')