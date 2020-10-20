# -*- coding: utf-8 -*-
"""

An IP address (version 4) takes the form w.x.y.z where w x y and z are numbers in the range 0
– 255, e.g. 192.168.34.10. It would be a mistake to any of the numbers was negative, or greater than
255.

Write a program which prompts the user to input a valid IP address. The program should use a
counting loop to input the 4 numbers of the IP address, and use an input validation loop to ensure
that the number is valid before proceeding. Once a valid number has been input, it should be added
to the IP address.

@author: kevmc
"""

result = ""

for i in range (0,4):
    
    number = int(input("Enter the value : \n"))
    
    while number < 0 or number > 255:
         number = int(input("Invalid entry, try again : \n"))
    
    if i <3 :   
        result += str(number) + "."    
    else:
        result += str(number)
        
print(result)

