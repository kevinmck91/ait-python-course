# -*- coding: utf-8 -*-
"""
Write a program which inputs 6 long jump distances displays the average, maximum and minimum
jump, without using a list or other data structure.

@author: kevmc
"""

count = 1
total = 0
minimum = 0
maximum = 0

while count <= 6 :
    
    distance = float(input(f"Enter the distance for jump no. {count} \n"))
     
    if count == 1:
        minimum = distance
        maximum = distance
    else :
        
        if distance < minimum:
            minimum = distance
        
        if distance >  maximum:
            maximum = distance
            
    total = total + distance
    count = count + 1

print("\nMinimum distance = ", minimum)
print("Maximum Distance = ", maximum)
print("total Distance = ", total)   
print("average Distance = ", total / 6)   
 