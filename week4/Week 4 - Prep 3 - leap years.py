# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:18:41 2020
Write a program which inputs two years, and then determines and displays whether or not each year
between them is a leap year.

@author: kevmc
"""


for i in range(1990, 2021):
    
    leap_year = False
    
    if i % 400 == 0:
        leap_year = True
        
    if i % 4 == 0 and not i % 100 == 0 :
        leap_year = True
    
    if leap_year:
        print(f"{i} is a leap year") 
    else :
        print(f"{i} is not a leap year") 

