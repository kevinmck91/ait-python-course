## Write a program which inputs the pass success percentages, stores them in a list, and then calculates
## and displays the average and the standard devation.

print(" \n ******** 4(a)  ******** \n ")

import math

list_of_pass_success_rates = [50.5, 84.0, 74.4, 71.2, 85.3, 41.7, 61.1, 71.4, 45.9, 90.4]
  
average = sum(list_of_pass_success_rates) / len(list_of_pass_success_rates)
    
value_minus_average = [ (x-average)**2 for x in list_of_pass_success_rates ]

result = sum(value_minus_average) / (len(list_of_pass_success_rates) - 1)

standard_deviation = math.sqrt(result)

print("average =" , average)
print ("standard_deviation = " , standard_deviation)