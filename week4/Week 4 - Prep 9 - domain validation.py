# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:20:16 2020

@author: kevmc
"""

domain = input("Enter the domain : \n")

valid_size = True
valid_symbols = True

if len(domain) > 100:
    valid_size = False


for character in domain:
    
    if valid_size == False :
        print("invalid length")
        break
    
    if character.isalnum():
        pass
    elif character == "." :
        pass
    elif character == "/" :
        pass
    elif character == "-" :
        pass
    else:
        print("invalid character")
        valid_symbols = False
        break
        
if(valid_symbols and valid_size):
     print("All good")
        
