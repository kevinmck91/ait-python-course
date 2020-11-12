## Write a program which inputs the pass success percentages, stores them in a list, and then calculates
## and displays the average and the standard devation.

print(" \n ******** 4(a)  ******** \n ")


x_passes_per_game     = [26.8, 62.4, 25.9, 9.10, 78.4, 23.4, 15.8, 44.1, 25.9, 54.9]
y_pass_success_rates  = [50.5, 84.0, 74.4, 71.2, 85.3, 41.7, 61.1, 71.4, 45.9, 90.4]

# Top line
average_x = sum(x_passes_per_game) / len(x_passes_per_game)
average_y = sum(y_pass_success_rates) / len(y_pass_success_rates)

deviations_for_x = [x - average_x for x in x_passes_per_game]
deviations_for_y = [y - average_y for y in y_pass_success_rates]

# For multiplying corrosponding values in the two lists
deviations_for_xy = [x*y for (x,y) in zip(deviations_for_x, deviations_for_y)]

print("\n deviations_for_x : " , deviations_for_x )
print("\n deviations_for_y : " , deviations_for_y )
print("\n deviations_for_xy : " , deviations_for_xy )

deviations_for_x_squ = [(x - average_x)**2 for x in x_passes_per_game]
deviations_for_y_squ = [(y - average_y)**2 for y in y_pass_success_rates]

import math

corralation = sum(deviations_for_xy) / math.sqrt((sum(deviations_for_x_squ))*(sum(deviations_for_y_squ)))

print(f"\n corralation : {corralation:.1f}" )