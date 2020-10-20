# -*- coding: utf-8 -*-
"""
Write a program which simulates registering a user account.
The user should be prompted to enter a valid username. A username is valid if it is at most 8
characters and contains no uppercase letters. Use a while loop to ensure that a valid username is
entered.

The user should then be prompted to enter his/her password, and again to confirm it. Use a while
loop to ensure that a) the two passwords match, and b) the password is at least 8 characters long.

Once a valid username and password has been entered, the message “Registration Complete” should
be displayed.

@author: kevmc
"""

username = ""
username_valid = False

while username_valid == False:
    
    username = input("Enter username \n")
    
    if len(username) >= 8:
        print("Username is too long")
        username_valid = False
        continue
    elif not username.islower():
        print("Username needs to be lower case")
        username_valid = False
        continue
    else:
        print("Username is fine")
        username_valid = True
        

password = ""
password_valid = False

while password_valid == False:
    
    password = input("Enter password \n")
    
    if len(password) < 8:
        print("password must be at lease 8 chars long")
        password_valid = False
        continue
    else:
        password_check = input("Enter password again \n")
        if password_check == password:
            print("passwords has been created")
            password_valid = True
        else:
             print("passwords do not match")
             password_valid = False

