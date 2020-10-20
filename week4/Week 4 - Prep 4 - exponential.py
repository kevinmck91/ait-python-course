# -*- coding: utf-8 -*-
"""
Write a program which calculates and displays:
– the number of grains of wheat on each square,
– and the total number of grains of wheat.

@author: kevmc
"""

grains = 1
total_grains = 0

for i in range(0,64):
    
    print(f"On square no. {i+1}, there are {grains} grains")
    
    total_grains += grains
    grains = grains*2
    
print(total_grains)

